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
"""Settings manager for VSCode."""

import os
from pathlib import Path
from typing import List, Dict, Any
from poetryx.file.file_manager import write_file, read_file_dict
from .settings_manager import SettingsManager


class VscodeSettingsManager(SettingsManager):
    """Manages VScode IDE settings for poetry environments.

    See https://code.visualstudio.com/docs/getstarted/settings
    for more information.
    """

    vscode_settings_dir: str = "./.vscode"
    setting_file_path: Path = Path(vscode_settings_dir, "setting.json")
    launch_file_path: Path = Path(vscode_settings_dir, "launch.json")

    @property
    def launch_file(self) -> Dict[str, Any]:
        return read_file_dict(self.launch_file_path, json=True)

    @property
    def setting_file(self) -> Dict[str, Any]:
        return read_file_dict(self.setting_file_path, json=True)

    def set_poetry_debugger(self, path: str) -> None:
        """Sets the poetry debugger in vscode to the given poetry path.

        It will create the .vscode directory if it doesn't exist and update the launch.json file
        if it exists.

        Args:
            path (str): The path to the poetry executable.
        """
        if os.path.exists(self.vscode_settings_dir) and os.path.exists(
            self.launch_file_path
        ):
            vscode_launch = self.launch_file
            vscode_launch = self._update_vscode_launch(vscode_launch, path)
        else:
            os.makedirs(self.vscode_settings_dir, exist_ok=True)
            vscode_launch = self._default_launch_settings(path)
        write_file(self.launch_file_path, vscode_launch, json=True)

    def _update_vscode_launch(
        self, vscode_launch: Dict[str, Any], path: str
    ) -> Dict[str, Any]:
        """Parse the launch file and determine what values need to be updated.

        Args:
            vscode_launch (Dict[str, Any]): The contents of the launch file.
            path (str): The path to the poetry executable.

        Returns:
            Dict[str, Any]: The updated launch file.
        """
        launch_settings: Dict[str, Any] = self._default_launch_settings(path)
        vscode_launch["version"] = vscode_launch.get(
            "version", launch_settings.get("version", "0.2.0")
        )
        configurations: List[Dict[str, Any]] = vscode_launch.get("configurations", [])

        debugpy_found = False
        for config in configurations:
            if config.get("type") == "debugpy":
                if config.get("env"):
                    config["env"].update(launch_settings["configurations"][0]["env"])
                else:
                    config["env"] = launch_settings["configurations"][0]["env"]
                debugpy_found = True

        if not debugpy_found:
            configurations.append(launch_settings["configurations"][0])

        vscode_launch["configurations"] = configurations
        return vscode_launch

    def _default_launch_settings(self, path: str) -> Dict[str, Any]:
        return {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Python: Current File",
                    "type": "debugpy",
                    "request": "launch",
                    "program": "${file}",
                    "console": "integratedTerminal",
                    "env": {
                        "PATH": path,
                        "PYSPARK_PYTHON": path,
                        "PYSPARK_DRIVER_PYTHON": path,
                    },
                }
            ],
        }
