import os
from pathlib import Path

from .file_manager import write_file, delete_file,read_file


class FileConfig:

    config_file: str = ".poetryx"
    config_template_toml: str = "config.toml"
    config_path: str = Path.joinpath(Path.home(), config_file)
    config_toml_path: str = Path.joinpath(Path(__file__).resolve().parent, config_template_toml)

    def __init__(self):
        self._validate_configuration()

    def _validate_configuration(self):
        if not os.path.exists(self.config_path):
            
            write_file(self.config_path, read_file(self.config_toml_path))

    def clean_configuration(self):
        delete_file(self.config_path)

    def set_configuration(self, config: dict):
        write_file(self.config_path, config, toml=True)