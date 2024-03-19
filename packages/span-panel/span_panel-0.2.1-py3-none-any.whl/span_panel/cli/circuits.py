from __future__ import annotations

from dataclasses import dataclass
from functools import cmp_to_key
from typing import Optional, cast

from rich.console import Console
from rich.table import Table
import typer

from span_panel.api import SpanClient
from span_panel.cli import base
from span_panel.client import models as d

app = typer.Typer(rich_markup_mode="rich")


ARG_CIRCUIT_ID = typer.Argument(
    None,
    help="ID of the circuit to select for subcommands",
)


@dataclass
class CircuitContext(base.CliContext):
    circuits: dict[str, d.Circuit] | None = None
    circuit: d.Circuit | None = None


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context, circuit_id: Optional[str] = ARG_CIRCUIT_ID) -> None:
    """SPAN panel circuit CLI."""

    base.require_auth(ctx)
    client = cast(SpanClient, ctx.obj.api)
    ctx.obj = CircuitContext(api=client, output_format=ctx.obj.output_format)

    async def callback() -> d.CircuitsOut:
        return await client.get_circuits()

    async def circuit_callback(cid: str) -> d.Circuit:
        return await client.get_circuit(cid)

    if not ctx.invoked_subcommand and (circuit_id is None or circuit_id == "list-ids"):
        response = base.run(ctx, callback())
        ctx.obj.circuits = response.circuits
        if circuit_id == "list-ids":
            ctx.invoke(list_ids, ctx)
        else:
            base.json_output(response.dict(by_alias=True))
    elif circuit_id is not None:
        ctx.obj.circuit = base.run(ctx, circuit_callback(circuit_id))
        if not ctx.invoked_subcommand:
            _print_circuit(ctx)


def require_circuit_id(ctx: typer.Context) -> None:
    """Requires circuit ID in context"""

    if ctx.obj.circuit is None:
        typer.secho("Requires a valid circuit ID to be selected", fg="red")
        raise typer.Exit(1)


def require_no_circuit_id(ctx: typer.Context) -> None:
    """Requires no circuit ID in context"""

    if ctx.obj.circuit is not None:
        typer.secho("Requires no circuit ID to be selected", fg="red")
        raise typer.Exit(1)


@app.command()
def list_ids(ctx: typer.Context) -> None:
    """Requires no circuit ID. Prints list of "id name" for each device."""

    require_no_circuit_id(ctx)
    circuits: dict[str, d.Circuit] = ctx.obj.circuits
    if not circuits:
        return

    to_print = [
        (c.id, c.tabs, c.name)
        for c in sorted(
            circuits.values(),
            key=cmp_to_key(lambda i1, i2: i1.tabs[0] - i2.tabs[0]),  # type: ignore[index,attr-defined]
        )
    ]
    if ctx.obj.output_format == base.OutputFormat.JSON:
        base.json_output(to_print)
    elif ctx.obj.output_format == base.OutputFormat.PLAIN:
        for item in to_print:
            typer.echo(f"{item[0]}\t{item[1]!s:8}\t{item[2]}")
    else:
        table = Table(title="Circuits", row_styles=["dim", ""])
        table.add_column("ID")
        table.add_column("Tabs")
        table.add_column("Name")
        for item in to_print:
            table.add_row(item[0], str(item[1]), item[2])

        Console().print(table)


def _print_circuit(ctx: typer.Context) -> None:
    require_circuit_id(ctx)
    circuit: d.Circuit = ctx.obj.circuit
    if not circuit:
        return

    if ctx.obj.output_format == base.OutputFormat.JSON:
        base.json_output(circuit.dict(by_alias=True))
    elif ctx.obj.output_format == base.OutputFormat.PLAIN:
        typer.echo(f"ID: {circuit.id}")
        typer.echo(f"Tabs: {circuit.tabs}")
        typer.echo(f"Name: {circuit.name}")
        typer.echo(f"Relay State: {circuit.relay_state.value}")
        typer.echo(f"Instant Power: {circuit.instant_power_w} w")
        typer.echo(
            f"Instant Power Update Time: {circuit.instant_power_update_time_s} s",
        )
        typer.echo(f"Produced Energy: {circuit.produced_energy_wh} wh")
        typer.echo(f"Consumed Energy: {circuit.consumed_energy_wh} wh")
        typer.echo(
            f"Energy Accumulation Update Time: {circuit.energy_accum_update_time_s} s",
        )
        typer.echo(f"Priority: {circuit.priority.value}")
        typer.echo(f"Is User Controllable: {circuit.is_user_controllable}")
        typer.echo(f"Is Sheddable: {circuit.is_sheddable}")
        typer.echo(f"Is Never Backup: {circuit.is_never_backup}")
    else:
        table = Table(title="Circuit", row_styles=["", "dim"], show_header=False)
        table.add_row("ID", circuit.id)
        table.add_row("Tabs", str(circuit.tabs))
        table.add_row("Name", circuit.name)
        table.add_row("Relay State", circuit.relay_state.value)
        table.add_row("Instant Power", str(circuit.instant_power_w) + " w")
        table.add_row(
            "Instant Power Update Time",
            str(circuit.instant_power_update_time_s) + " s",
        )
        table.add_row("Produced Energy", str(circuit.produced_energy_wh) + " wh")
        table.add_row("Consumed Energy", str(circuit.consumed_energy_wh) + " wh")
        table.add_row("Energy Accumulation Update Time", str(circuit.id) + " s")
        table.add_row("Priority", circuit.priority.value)
        table.add_row("Is User Controllable", str(circuit.id))
        table.add_row("Is Sheddable", str(circuit.id))
        table.add_row("Is Never Backup", str(circuit.id))

        Console().print(table)


@app.command()
def relay_state(
    ctx: typer.Context,
    relay_state: Optional[d.RelayState] = typer.Argument(None),
) -> None:
    """Get or Set Relay State."""

    require_circuit_id(ctx)
    circuit: d.Circuit = ctx.obj.circuit
    client = cast(SpanClient, ctx.obj.api)
    if not circuit:
        return

    async def callback(state: d.RelayState) -> d.Circuit:
        return await client.set_circuit_by_values(
            circuit_id=circuit.id,
            relay_state=state,
        )

    if relay_state is not None:
        circuit = base.run(ctx, callback(relay_state))

    if ctx.obj.output_format == base.OutputFormat.JSON:
        base.json_output(circuit.relay_state.value)
    else:
        typer.echo(circuit.relay_state.value)
