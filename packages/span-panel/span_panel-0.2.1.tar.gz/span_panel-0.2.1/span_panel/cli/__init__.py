from __future__ import annotations

import logging
import sys
from typing import Annotated, Optional, cast

from rich.console import Console
from rich.style import Style
from rich.table import Table
import typer

from span_panel.api import SpanClient
from span_panel.cli.base import (
    OPTION_FORCE,
    CliContext,
    OutputFormat,
    json_output,
    require_auth,
    run,
)
from span_panel.cli.circuits import app as circuits_cli
from span_panel.cli.panel import app as panel_cli
from span_panel.cli.storage import app as storage_cli
from span_panel.client import models as d

_LOGGER = logging.getLogger("span_panel")

try:
    from IPython import embed
    from termcolor import colored
    from traitlets.config import get_config
except ImportError:
    embed = termcolor = get_config = None  # type: ignore[assignment]

OPTION_HOST = typer.Option(
    ...,
    "--host",
    "-h",
    help="Base URL for SPAN Panel",
    prompt=True,
    envvar="SPAN_HOST",
)
OPTION_TOKEN = typer.Option(
    None,
    "--token",
    "-t",
    help="SPAN panel token",
    prompt=False,
    envvar="SPAN_TOKEN",
)
OPTION_OUT_FORMAT = typer.Option(
    OutputFormat.RICH,
    "--output-format",
    help="Preferred output format. Not all commands support both JSON and plain and may still output in one or the other.",
    envvar="SPAN_OUTPUT_FORMAT",
)

ARGUMENT_NAME = Annotated[
    str,
    typer.Argument(
        help="Alphanumeric field with the name of your client. Should be unique.",
    ),
]
OPTION_DESCRIPTION = typer.Option(
    None,
    "--description",
    "-d",
    help="Optional description of client.",
)
BYPASS_INSTRUCTIONS = """
To initate a proximity bypass, open and close the door on your panel 3 times.
The lights inside of the panel should start flashing. The bypass will remain
active for 15 minutes. Once it is active, you can generate an auth token to use.
"""


app = typer.Typer(rich_markup_mode="rich")
app.add_typer(storage_cli, name="storage")
app.add_typer(panel_cli, name="panel")
app.add_typer(circuits_cli, name="circuits")


@app.callback()
def main(
    ctx: typer.Context,
    host: str = OPTION_HOST,
    token: Optional[str] = OPTION_TOKEN,
    output_format: OutputFormat = OPTION_OUT_FORMAT,
) -> None:
    """SPAN Panel CLI"""

    span = SpanClient(host=host, token=token)
    ctx.obj = CliContext(api=span, output_format=output_format)


def _setup_logger(level: int = logging.DEBUG, show_level: bool = False) -> None:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    if show_level:
        formatter = logging.Formatter("%(levelname)s: %(message)s")
        console_handler.setFormatter(formatter)
    _LOGGER.setLevel(logging.DEBUG)
    _LOGGER.addHandler(console_handler)


@app.command()
def shell(ctx: typer.Context) -> None:
    """Opens iPython shell with Protect client initialized.

    Requires the `shell` extra to also be installed.
    """

    require_auth(ctx)
    if embed is None or colored is None:
        typer.echo("ipython and termcolor required for shell subcommand")
        sys.exit(1)

    # locals passed to shell
    client = cast(  # noqa:F841
        SpanClient,
        ctx.obj.api,
    )
    _setup_logger(show_level=True)

    c = get_config()
    c.InteractiveShellEmbed.colors = "Linux"
    embed(  # type: ignore[no-untyped-call]
        header=colored("client = SpanClient(*args)", "green"),
        config=c,
        using="asyncio",
    )


def _prompt_bypass() -> None:
    default = False

    response = False
    while not response:
        response = typer.confirm(
            typer.style(
                "Have to initiated a proximity bypass within the last 15 minutes (no to explain how)?",
                fg="green",
            ),
            default=default,
        )
        if not response:
            default = True
            typer.echo(BYPASS_INSTRUCTIONS)


@app.command()
def generate_token(
    ctx: typer.Context,
    name: ARGUMENT_NAME,
    force: bool = OPTION_FORCE,
    description: Optional[str] = OPTION_DESCRIPTION,
) -> None:
    """Generate an auth token to use to interact with the SPAN Panel API.

    Requires a proximity bypass. To initate a proximity bypass, open and close
    the door on your panel 3 times. The lights inside of the panel should start
    flashing. The bypass will remain active for 15 minutes. Once it is active, you can
    generate an auth token to use.
    """

    if not force:
        _prompt_bypass()

    client = cast(SpanClient, ctx.obj.api)

    async def callback() -> d.AuthOut:
        return await client.generate_token(name=name, description=description)

    response = run(ctx, callback())
    if ctx.obj.output_format == OutputFormat.JSON:
        json_output(response.dict(by_alias=True))
    else:
        typer.echo(response.access_token)


@app.command()
def islanding(ctx: typer.Context) -> None:
    """Get islanding state."""

    client = cast(SpanClient, ctx.obj.api)

    async def callback() -> d.IslandingState:
        return await client.get_islanding_state()

    response = run(ctx, callback())
    if ctx.obj.output_format == OutputFormat.JSON:
        json_output(response.dict(by_alias=True))
    else:
        typer.echo(response.islanding_state)


@app.command()
def main_relay(ctx: typer.Context) -> None:
    """Get main relay state."""

    client = cast(SpanClient, ctx.obj.api)

    async def callback() -> d.RelayStateOut:
        return await client.get_main_relay_state()

    response = run(ctx, callback())
    if ctx.obj.output_format == OutputFormat.JSON:
        json_output(response.dict(by_alias=True))
    else:
        typer.echo(response.relay_state)


@app.command()
def status(ctx: typer.Context) -> None:
    """Get system status."""

    client = cast(SpanClient, ctx.obj.api)

    async def callback() -> d.StatusOut:
        return await client.get_system_status()

    response = run(ctx, callback())
    if ctx.obj.output_format == OutputFormat.JSON:
        json_output(response.dict(by_alias=True))
    elif ctx.obj.output_format == OutputFormat.PLAIN:
        typer.echo("Software:")
        typer.echo(f"  Firmware Version: {response.software.firmware_version}")
        typer.echo(f"  Update Status: {response.software.update_status}")
        typer.echo(f"  Env: {response.software.env}")
        typer.echo("System:")
        typer.echo(f"  Manufacturer: {response.system.manufacturer}")
        typer.echo(f"  Serial: {response.system.serial}")
        typer.echo(f"  Model: {response.system.model}")
        typer.echo(f"  Door State: {response.system.door_state}")
        typer.echo(f"  Proximity Proven: {response.system.proximity_proven}")
        typer.echo(f"  Uptime: {response.system.uptime}")
        typer.echo("Network:")
        typer.echo(f"  Ethernet: {response.network.eth0_link}")
        typer.echo(f"  WiFi: {response.network.wlan_link}")
        typer.echo(f"  Celluar: {response.network.wwan_link}")
    else:
        table = Table(title="System Status", row_styles=["dim", ""], show_header=False)
        table.add_row("Software", style=Style(bold=True, dim=False))
        table.add_section()
        table.add_row(
            "Firmware Version",
            str(response.software.firmware_version),
        )
        table.add_row(
            "Update Status",
            str(response.software.update_status),
        )
        table.add_row(
            "Env",
            str(response.software.env),
        )
        table.add_section()
        table.add_row("Software", style=Style(bold=True, dim=False))
        table.add_section()
        table.add_row(
            "Manufacturer",
            str(response.system.manufacturer),
        )
        table.add_row(
            "Serial",
            str(response.system.serial),
        )
        table.add_row(
            "Model",
            str(response.system.model),
        )
        table.add_row(
            "Door State",
            str(response.system.door_state),
        )
        table.add_row(
            "Proximity Proven",
            str(response.system.proximity_proven),
        )
        table.add_row(
            "Uptime",
            str(response.system.uptime),
        )
        table.add_section()
        table.add_row("Network", style=Style(bold=True, dim=False))
        table.add_section()
        table.add_row(
            "Ethernet",
            str(response.network.eth0_link),
        )
        table.add_row(
            "WiFi",
            str(response.network.wlan_link),
        )
        table.add_row(
            "Celluar",
            str(response.network.wwan_link),
        )

        Console().print(table)
