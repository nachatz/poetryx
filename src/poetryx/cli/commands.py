import typer
from .typer_cli import TyperCLI

app = TyperCLI()
cli = app.cli

@cli.command()
def configure():
    """ Configure poetryx configuration file """
    app.configure()

@cli.command()
def clean():
    """ Cleans up and resets poetryx to its initial state.
        Helpful if anything ever goes wrong!
     """
    confirmed = typer.confirm("🚨 Are you sure you want to wipe your config file (.poetryx)?")

    if confirmed:
        app.config.clean_configuration()
        typer.echo("Successfully reset poetryx")
    else:
        typer.echo("Cancelled reset")
