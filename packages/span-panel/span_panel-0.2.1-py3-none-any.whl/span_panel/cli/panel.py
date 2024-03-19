from __future__ import annotations

from typing import cast

from rich.console import Console
from rich.style import Style
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
def power(ctx: typer.Context) -> None:
    """Get the power for the SPAN Panel."""

    client = cast(SpanClient, ctx.obj.api)

    async def callback() -> d.PanelPower:
        return await client.get_panel_power()

    response = base.run(ctx, callback())

    if ctx.obj.output_format == base.OutputFormat.JSON:
        base.json_output(response.dict(by_alias=True))
    elif ctx.obj.output_format == base.OutputFormat.PLAIN:
        typer.echo(f"Instant Grid Power: {response.instant_grid_power_w} w")
        typer.echo(f"Feedthrough Power: {response.feedthrough_power_w} w")
    else:
        table = Table(title="Panel Power", row_styles=["dim", ""], show_header=False)
        table.add_row("Instant Grid Power", str(response.instant_grid_power_w) + " w")
        table.add_row("Feedthrough Power", str(response.instant_grid_power_w) + " w")

        Console().print(table)


@app.command()
def meter(ctx: typer.Context) -> None:
    """Get a meter read for the SPAN Panel."""

    client = cast(SpanClient, ctx.obj.api)

    async def callback() -> d.PanelMeter:
        return await client.get_panel_meter()

    response = base.run(ctx, callback())

    if ctx.obj.output_format == base.OutputFormat.JSON:
        base.json_output(response.dict(by_alias=True))
    elif ctx.obj.output_format == base.OutputFormat.PLAIN:
        typer.echo("Main Meter:")
        typer.echo(f"  Produced: {response.main_meter.produced_energy_wh} wh")
        typer.echo(f"  Consumed: {response.main_meter.consumed_energy_wh} wh")
        typer.echo("Feedthrough:")
        typer.echo(f"  Produced: {response.feedthrough.produced_energy_wh} wh")
        typer.echo(f"  Consumed: {response.feedthrough.consumed_energy_wh} wh")
    else:
        table = Table(title="Panel Meter", row_styles=["dim", ""], show_header=False)
        table.add_row("Main Meter", style=Style(bold=True, dim=False))
        table.add_section()
        table.add_row("Produced", str(response.main_meter.produced_energy_wh) + " wh")
        table.add_row("Consumed", str(response.main_meter.consumed_energy_wh) + " wh")
        table.add_section()
        table.add_row("Feedthrough", style=Style(bold=True, dim=False))
        table.add_section()
        table.add_row("Produced", str(response.feedthrough.produced_energy_wh) + " wh")
        table.add_row("Consumed", str(response.feedthrough.consumed_energy_wh) + " wh")

        Console().print(table)


def _make_state_table(response: d.PanelState) -> Table:
    table = Table(title="Panel State", row_styles=["dim", ""], show_header=False)
    table.add_column("", justify="left")
    table.add_column("", justify="left")
    table.add_column("", justify="right")
    table.add_row(
        "Main Relay",
        "State",
        response.main_relay_state.value,
    )
    table.add_row(
        "",
        "Produced",
        str(response.main_meter_energy.produced_energy_wh) + " wh",
    )
    table.add_row(
        "",
        "Consumed",
        str(response.main_meter_energy.consumed_energy_wh) + " wh",
    )
    table.add_section()

    table.add_row(
        "Instant Grid Power",
        "",
        str(response.instant_grid_power_w) + " w",
    )
    table.add_section()

    table.add_row(
        "Feedthrough",
        "Power",
        str(response.feedthrough_power_w) + " w",
    )
    table.add_row(
        "",
        "Produced",
        str(response.feedthrough_energy.produced_energy_wh) + " wh",
    )
    table.add_row(
        "",
        "Consumed",
        str(response.feedthrough_energy.consumed_energy_wh) + " wh",
    )
    table.add_section()

    table.add_row(
        "Grid Sample",
        "Start",
        str(response.grid_sample_start_ms) + " ms",
    )
    table.add_row(
        "",
        "End",
        str(response.grid_sample_end_ms) + " ms",
    )
    table.add_section()

    table.add_row(
        "",
        "DSM Grid State",
        str(response.dsm_grid_state),
    )
    table.add_row(
        "",
        "DSM State",
        str(response.dsm_state),
    )
    table.add_row(
        "",
        "Current Run Config",
        str(response.current_run_config),
    )
    table.add_section()

    table.add_row("Branches", style=Style(bold=True, dim=False))
    table.add_section()

    for branch in response.branches:
        table.add_row(
            "",
            "ID",
            str(branch.id),
        )
        table.add_row(
            "",
            "State",
            branch.relay_state.value,
        )
        table.add_row(
            "",
            "Instant Power",
            str(branch.instant_power_w) + " w",
        )
        table.add_row(
            "",
            "Imported Active Energy",
            str(branch.imported_active_energy_wh) + " wh",
        )
        table.add_row(
            "",
            "Exported Active Energy",
            str(branch.exported_active_energy_wh) + " wh",
        )
        table.add_row(
            "",
            "Measure Start",
            str(branch.measure_start_ts_ms) + " ms",
        )
        table.add_row(
            "",
            "Measure Duration",
            str(branch.measure_duration_ms) + " ms",
        )
        table.add_row(
            "",
            "Is Valid",
            str(branch.is_measure_valid),
        )
        table.add_section()

    return table


@app.command()
def state(ctx: typer.Context) -> None:
    """Get the current SPAN Panel state."""

    client = cast(SpanClient, ctx.obj.api)

    async def callback() -> d.PanelState:
        return await client.get_panel()

    response = base.run(ctx, callback())

    if ctx.obj.output_format == base.OutputFormat.JSON:
        base.json_output(response.dict(by_alias=True))
    elif ctx.obj.output_format == base.OutputFormat.PLAIN:
        typer.echo("Main Relay:")
        typer.echo(f"  State: {response.main_relay_state.value}")
        typer.echo(f"  Produced: {response.main_meter_energy.produced_energy_wh} wh")
        typer.echo(f"  Consumed: {response.main_meter_energy.consumed_energy_wh} wh")
        typer.echo(f"Instant Grid Power: {response.instant_grid_power_w} w")
        typer.echo("Feedthrough:")
        typer.echo(f"  Power: {response.feedthrough_power_w} w")
        typer.echo(f"  Produced: {response.feedthrough_energy.produced_energy_wh} wh")
        typer.echo(f"  Consumed: {response.feedthrough_energy.consumed_energy_wh} wh")
        typer.echo("Grid Sample:")
        typer.echo(f"  Start: {response.grid_sample_start_ms} ms")
        typer.echo(f"  End: {response.grid_sample_end_ms} ms")
        typer.echo(f"DSM Grid State: {response.dsm_grid_state}")
        typer.echo(f"DSM State: {response.dsm_state}")
        typer.echo(f"Current Run Config: {response.current_run_config}")
        typer.echo("Branches:")
        for branch in response.branches:
            branch = cast(d.Branch, branch)
            typer.echo(f"  Branch {branch.id}:")
            typer.echo(f"    State: {branch.relay_state.value}")
            typer.echo(f"    Instant Power: {branch.instant_power_w} w")
            typer.echo(
                f"    Imported Active Energy: {branch.imported_active_energy_wh} wh",
            )
            typer.echo(
                f"    Exported Active Energy: {branch.exported_active_energy_wh} wh",
            )
            typer.echo(
                f"    Measure Start: {branch.measure_start_ts_ms} ms",
            )
            typer.echo(
                f"    Measure Duration: {branch.measure_duration_ms} ms",
            )
            typer.echo(
                f"    Is Valid: {branch.is_measure_valid}",
            )
    else:
        Console().print(_make_state_table(response))
