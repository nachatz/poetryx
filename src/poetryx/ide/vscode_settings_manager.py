import os
from pathlib import Path
from .settings_manager import SettingsManager
from poetryx.file.file_manager import write_file, read_file
from typing import List, Dict, Any


class VscodeSettingsManager(SettingsManager):

    @property
    def vscode_settings_dir(self) -> str:
        return "./.vscode"

    @property
    def launch_file_path(self) -> str:
        return Path(self.vscode_settings_dir, "launch.json").as_posix()

    @property
    def setting_file_path(self) -> str:
        return Path(self.vscode_settings_dir, "setting.json").as_posix()

    @property
    def launch_file(self) -> Dict[str, Any]:
        return read_file(self.launch_file_path, json=True)

    @property
    def setting_file(self) -> str:
        return read_file(self.setting_file_path, json=True)

    def set_poetry_debugger(self, path: str) -> None:
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
