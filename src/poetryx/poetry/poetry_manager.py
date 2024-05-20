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
"""Class to manage poetry interactions."""

from poetryx.utils.cli import run_cli_command


class PoetryManager:
    """Manages the poetry CLI."""
    def get_virtualenv_path(self) -> str:
        path = run_cli_command(["poetry", "env", "info", "-p"])

        if path:
            return path
        raise ValueError("Unable to find virtualenv path")
