from __future__ import annotations

from typing import Optional, cast

from rich.console import Console
from rich.table import Table
import typer

from span_panel.api import SpanClient
from span_panel.cli import base
from span_panel.client import models as d

app = typer.Typer(rich_markup_mode="rich")


@app.callback()
def main(ctx: typer.Context) -> None:
    """SPAN panel storage CLI."""

    base.require_auth(ctx)


@app.command()
def nice_to_have_threshold(
    ctx: typer.Context,
    *,
    low: Optional[int] = typer.Argument(None),
    high: Optional[int] = typer.Argument(None),
) -> None:
    """Get or set the nice to have threshold.

    Passing low/high will set the thresholds. Not passing them will get the current
    thresholds.
    """

    if (low is not None and high is None) or (low is not None and high is None):
        typer.secho("low and high must both be passed or both not be passed", fg="red")
        raise typer.Exit(code=1)

    client = cast(SpanClient, ctx.obj.api)

    async def callback() -> d.NiceToHaveThreshold:
        if low is None or high is None:
            return await client.get_storage_nice_to_have_threshold()
        return await client.set_storage_nice_to_have_threshold(low=low, high=high)

    response = base.run(ctx, callback())

    if ctx.obj.output_format == base.OutputFormat.JSON:
        base.json_output(response.dict(by_alias=True))
    elif ctx.obj.output_format == base.OutputFormat.PLAIN:
        if response.nice_to_have_threshold_low_soe:
            typer.echo(
                f"Low Threshold: {response.nice_to_have_threshold_low_soe.percentage}",
            )
        if response.nice_to_have_threshold_high_soe:
            typer.echo(
                f"High Threshold: {response.nice_to_have_threshold_high_soe.percentage}",
            )
    else:
        table = Table(title="Nice to Have", row_styles=["dim", ""])

        table.add_column("Type")
        table.add_column("Threshold")

        if response.nice_to_have_threshold_low_soe:
            table.add_row(
                "Low",
                str(response.nice_to_have_threshold_low_soe.percentage) + " %",
            )
        if response.nice_to_have_threshold_high_soe:
            table.add_row(
                "High",
                str(response.nice_to_have_threshold_high_soe.percentage) + " %",
            )

        Console().print(table)


@app.command()
def soe(ctx: typer.Context) -> None:
    """Get the state of energy (soe)."""

    client = cast(SpanClient, ctx.obj.api)

    async def callback() -> d.BatteryStorage:
        return await client.get_storage_level()

    response = base.run(ctx, callback())

    if ctx.obj.output_format == base.OutputFormat.JSON:
        base.json_output(response.dict(by_alias=True))
    elif ctx.obj.output_format == base.OutputFormat.PLAIN:
        typer.echo(response.soe.percentage)
    else:
        typer.echo(f"State of Energy: {response.soe.percentage} %")
