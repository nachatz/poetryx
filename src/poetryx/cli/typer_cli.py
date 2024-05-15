import typer
import click
from poetryx.file import FileConfig
from poetryx.file.file_config import read_file, write_file

class TyperCLI:

    """ Custom typer CLI """

    def __init__(self):
        self.cli = typer.Typer()
        self.config = FileConfig()

    def configure(self):
        """ Configure poetryx """
        toml = read_file(FileConfig.config_path, toml=True)
        config = toml["poetryx"]["config"]
        def prompt(option, options=[]):
            click_choice = click.Choice(options)
            resp: click.Choice = typer.prompt(
                f"{option.upper()}",
                default=config[option],
                show_choices=True,
                type=click_choice
            )
            config[option] = resp

        prompt("ide", ["vscode", "n/a"])

        result = {"poetryx": {"config": config }}
        write_file(FileConfig.config_path, result, toml=True)