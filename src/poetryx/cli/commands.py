# Copyright 2024 Nikolas Achatz (github.com/nachatz)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Commands interface that provide the entry point for poetryx."""

import typer
from json import JSONDecodeError
from .typer_cli import TyperCLI


app = TyperCLI()
cli = app.cli


@cli.command()
def setup() -> None:
    """Setup poetryx configuration file"""
    app.setup()


@cli.command()
def clean() -> None:
    """Cleans up and resets poetryx to its initial state.
    Helpful if anything ever goes wrong!
    """
    confirmed = typer.confirm(
        "🚨 Are you sure you want to wipe your config file (.poetryx)?"
    )

    if confirmed:
        app.config.clean_configuration()
        typer.echo("Successfully reset poetryx")
    else:
        typer.echo("Cancelled reset")


@cli.command()
def configure() -> None:
    """Setup IDE environment to use the current poetry environment"""

    if "vscode" not in app.config.ide:
        typer.echo("Only vscode supported at the moment")
        return

    typer.echo("Setting your IDE environment to use the current poetry environment")
    if typer.confirm(
        "🚨 Are you at the root of your project (where you want a .vscode)?"
    ):
        try:
            path = app.poetry.get_virtualenv_path()
            app.settings_obj.set_poetry_debugger(path)
            typer.echo(f"VScode debugger setup for: {path}")
        except JSONDecodeError:
            typer.echo(
                "Invalid JSON present in current .vscode directory (check settings/launch.json)"
            )
        except Exception as e:
            typer.echo(f"Failed to set VScode debugger: {e}")
