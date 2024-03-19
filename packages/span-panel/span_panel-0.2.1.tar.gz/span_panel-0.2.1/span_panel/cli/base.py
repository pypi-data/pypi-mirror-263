from __future__ import annotations

import asyncio
from collections.abc import Coroutine
from dataclasses import dataclass
from enum import Enum
from typing import Any, TypeVar

import orjson
import typer

from span_panel.api import SpanClient
from span_panel.exceptions import SpanError

OPTION_FORCE = typer.Option(False, "-f", "--force", help="Skip confirmation prompt")


class OutputFormat(str, Enum):
    JSON = "json"
    PLAIN = "plain"
    RICH = "rich"


T = TypeVar("T")


@dataclass
class CliContext:
    api: SpanClient
    output_format: OutputFormat


def json_output(obj: Any) -> None:
    typer.echo(orjson.dumps(obj, option=orjson.OPT_INDENT_2).decode("utf-8"))


def run(ctx: typer.Context, func: Coroutine[Any, Any, T]) -> T:
    """Helper method to call async function and clean up API client"""

    async def callback() -> T:
        try:
            return_value = await func
        finally:
            await ctx.obj.api.close_session()
        return return_value

    try:
        return asyncio.run(callback())
    except SpanError as err:
        typer.secho(str(err), fg="red")
        raise typer.Exit(1) from err


def require_auth(ctx: typer.Context) -> None:
    if not ctx.obj.api.has_auth:
        typer.secho(
            "Token missing. To generate a new token, run `span-panel generate-token`",
            fg="red",
        )
        raise typer.Exit(code=1)
