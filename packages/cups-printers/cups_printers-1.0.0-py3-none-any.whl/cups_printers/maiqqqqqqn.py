"""Main part of cups-pinters."""
import typer
from typing_extensions import Annotated
from validators import url

from cups_printers.commands import output, queue, state
from cups_printers.constants import DEFAULT_SERVER, TIMEOUT

app = typer.Typer()

app.add_typer(output.app, name="output")
app.add_typer(queue.app, name="queue")
app.add_typer(state.app, name="state")


def validate_host(value: str):
    """Check if host is a valid URL."""
    if url(value):
        raise typer.BadParameter("URL is not valid")
    return value


def validate_key(value: str):
    """Check the length of an API key."""
    if len(value) != 64:
        raise typer.BadParameter("Key doesn't have the right length")
    return value


@app.callback()
def main(
    ctx: typer.Context,
    server: Annotated[
        str,
        typer.Option(
            envvar="CUPS_SERVER",
            help="The server URL of CUPS instance",
            prompt=True,
            callback=validate_host,
        ),
    ] = DEFAULT_SERVER,
    timeout: Annotated[
        str,
        typer.Option(
            envvar="TIMEOUT",
            help="Timeout for network operations",
            prompt=True,
            callback=validate_key,
        ),
    ] = TIMEOUT,
):
    try:
        cups.setServer(server)
        ctx.obj = {"connection": cups.Connection()}
    except RuntimeError:
        typer.echo("Server not available or unable to connect")
        raise SystemExit


if __name__ == "__main__":
    app()
