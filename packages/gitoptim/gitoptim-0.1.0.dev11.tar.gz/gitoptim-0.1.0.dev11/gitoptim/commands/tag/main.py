from typing import Annotated, Optional

import typer

from gitoptim.utils.cli import should_callback_execute, error_console

from .start import command as start
from .end import command as end

app = typer.Typer(rich_markup_mode="rich")


def validate_name(name: Optional[str]):
    if name is not None and len(name) == 0:
        error_console.print("Name cannot be empty.")
        raise typer.Exit(code=1)

    elif name is not None and name.isalnum() is False:
        error_console.print("Name can only contain letters and numbers.")
        raise typer.Exit(code=1)

    return name


@app.callback()
def main(ctx: typer.Context, name: Annotated[str, typer.Option(help="name", callback=validate_name)] = None):
    """
    Analyse code or Gitlab job logs.
    """

    if not should_callback_execute():
        return

    ctx.obj = {"name": name}


app.command(name="start")(start)
app.command(name="end")(end)
