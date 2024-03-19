import asyncio
import contextlib
import json
import sys
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from functools import wraps
from pathlib import Path
from types import EllipsisType
from typing import Any, TypeVar

import typer
from camel_converter import to_snake
from tabulate import tabulate
from validio_sdk import config
from validio_sdk.config import Config, ValidioConfig
from validio_sdk.util import ClassJSONEncoder
from validio_sdk.validio_client import ValidioAPIClient

F = TypeVar("F", bound=Callable[..., Any])
T = TypeVar("T", bound="OutputSettings")

DEFAULT_NAMESPACE: str = "default"


class OutputFormat(str, Enum):
    """Available output formats for the CLI"""

    JSON = "json"
    TEXT = "text"


# Shared command line argument and flag types.
ConfigDir = typer.Option(
    config.default_config_dir,
    "--config-dir",
    "-c",
    help="Path to where config is stored",
)
OutputFormatOption = typer.Option(
    OutputFormat.TEXT.value, "--output", "-o", help="Output format"
)
Identifier = typer.Argument(
    default=None, help="Name or ID of the resource to get of this type"
)


# ruff: noqa: N802
# Let's use capital name to be consistent.
def Namespace(
    default: str | EllipsisType | None = None, help: str = "Namespace to target"
) -> Any:  # typer returns Any here
    """
    Create a namespace flag that defaults to optional with a short help
    text. Accepts a string, ellipsis or None and a help text.

    :param default: The default value (or ellipsis for required)
    :param help: Help text for the flag
    """
    return typer.Option(default, "--namespace", "-n", help=help)


class AsyncTyper(typer.Typer):
    """
    Async version of typer.

    Decorator to support running async functions with typer, will basically just
    wrap your function in `asyncio.run`
    """

    def async_command(self, *args: Any, **kwargs: Any) -> Callable:
        def decorator(async_func: F) -> F:
            @wraps(async_func)
            def sync_func(*_args: Any, **_kwargs: Any) -> None:
                return asyncio.run(async_func(*_args, **_kwargs))

            self.command(*args, **kwargs)(sync_func)
            return async_func

        return decorator


async def get_client_and_config(
    config_dir: str = ConfigDir,
) -> tuple[ValidioAPIClient, ValidioConfig]:
    cfg = Config(Path(config_dir)).read()
    vc = ValidioAPIClient(validio_config=cfg)

    return (vc, cfg)


@dataclass
class OutputSettings:
    attribute_name: str | None = None
    reformat: Callable[[Any], Any] | None = None
    pass_full_object: bool = False

    @classmethod
    def trimmed_upper_snake(cls: type[T], attribute_name: str | None, trim: str) -> T:
        return cls(
            attribute_name=attribute_name,
            reformat=lambda x: to_snake(x.removesuffix(trim)).upper(),
        )


def output_json(obj: Any, identifier: str | None = None) -> None:
    # If we have an identifier we only want to display a single object so grab
    # the first index if object is not empty and is a list.
    if obj is not None and isinstance(obj, list) and identifier is not None:
        with contextlib.suppress(IndexError):
            obj = obj[0]

    j = json.dumps(obj, sort_keys=True, indent=2, cls=ClassJSONEncoder)
    print(j)


def output_text(items: Any, fields: dict[str, OutputSettings | None]) -> None:
    if items is None:
        items = []
    elif not isinstance(items, list):
        items = [items]

    table: list[list[str]] = [[k.upper().replace("_", " ") for k in fields]]

    for item in items:
        row = []
        for field_name, settings in fields.items():
            attribute_name = field_name
            if settings is not None and settings.attribute_name is not None:
                attribute_name = settings.attribute_name

            if settings and settings.pass_full_object and settings.reformat:
                row.append(settings.reformat(item))
                continue

            if not hasattr(item, attribute_name):
                row.append("UNKNOWN")
                continue

            value = getattr(item, attribute_name)
            if isinstance(value, datetime):
                value = _format_relative_time(value)

            if settings is not None and settings.reformat is not None:
                value = settings.reformat(value)

            row.append(value)

        table.append(row)

    datatable = tabulate(table, tablefmt="plain")
    print(datatable)

    # We flush stdout here so we can avoid an unhandled broken pipe error.
    # Catching the exception according to the documentation at
    # https://docs.python.org/3/library/signal.html#note-on-sigpipe does not
    # work in this context. Generating a table with the same amount of data but
    # without iterating over the object (i.e. adding a static string) does not
    # cause this issue so it must be related to the content.
    #
    # This is important to allow piping to commands like `head` without getting
    # a message on stderr about unhandled exceptions for the broken pipe.
    # Internal ref: VR-2146
    sys.stdout.flush()


# ruff: noqa: PLR2004, PLR0911
def _format_relative_time(d: datetime) -> str:
    diff = datetime.now(timezone.utc) - d
    seconds = diff.seconds

    if diff.days < 0:
        return "0s"
    if diff.days >= 1:
        return f"{diff.days}d"
    if seconds <= 1:
        return "1s"
    if seconds < 60:
        return f"{seconds}s"
    if seconds < 120:
        return "1m"
    if seconds < 3600:
        return f"{int(seconds/60)}m"
    if seconds < 7200:
        return "1h"

    return f"{int(seconds/3600)}h"


def _single_resource_if_specified(items: list[Any], identifier: str | None) -> Any:
    if identifier is None:
        return items

    return next(
        (
            item
            for item in items
            if (hasattr(item, "resource_name") and item.resource_name == identifier)
            or (hasattr(item, "name") and item.name == identifier)
            or item.id == identifier
        ),
        None,
    )


def _resource_filter(
    resource: Any | None,
    field_path: list[str],
    value: str | None,
) -> bool:
    # If we don't have an object we don't want to filter it in.
    if resource is None:
        return False

    # If we don't have a value to filter for we don't want to filter it out.
    if value is None:
        return True

    # Traverse the object til the resource we need for filtering.
    for field in field_path:
        # If the object doesn't even have the field we can't do comparison so filter
        # it out.
        if not hasattr(resource, field):
            return False

        resource = getattr(resource, field)
        # If the object field value we need for filtering out is none we filter
        # it out.
        if resource is None:
            return False

    return value in (resource.id, resource.resource_name)


def _fixed_width(message: str, width: int = 25) -> str:
    message = f"{message}: "
    return f"{message:<{width}} "
