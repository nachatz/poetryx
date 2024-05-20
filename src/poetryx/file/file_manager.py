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
"""Utilities for reading and writing files."""

import os
from typing import Dict, Any
from pathlib import Path
from json import load as json_load, dump as json_dump, JSONDecodeError
from toml import load as toml_load, dump as toml_dump, TomlDecodeError

def read_file_dict(
    path: Path, toml: bool = False, json: bool = False
) -> Dict[str, Any]:
    if toml and json:
        raise ValueError("Only one of 'toml' or 'json' can be True, not both.")

    try:
        with open(path, "r", encoding="utf-8") as file:
            if toml:
                return toml_load(file)
            if json:
                return dict(json_load(file))
            raise ValueError(
                    "Either 'toml' or 'json' must be True to return a dictionary."
                )
    except TomlDecodeError as e:
        raise TomlDecodeError(f"Invalid toml present in '{path}': {e}", e.doc, e.pos) from e
    except JSONDecodeError as e:
        raise JSONDecodeError(f"Invalid json present in '{path}': {e}", e.doc, e.pos) from e
    except Exception as e:
        raise Exception(f"Failed to read '{path}': {e}") from e


def read_file_raw(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        raise Exception(f"Failed to read '{path}': {e}") from e


def write_file(
    path: Path, content: str | Dict[str, Any], toml: bool = False, json: bool = False
) -> None:
    if toml and json:
        raise ValueError("Only one of 'toml' or 'json' can be True, not both.")

    with open(path, "w", encoding="utf-8") as file:
        if toml and isinstance(content, dict):
            toml_dump(content, file)
        elif json and isinstance(content, dict):
            json_dump(content, file, indent=4)
        elif not toml and isinstance(content, str):
            file.write(content)
        else:
            raise ValueError(
                "Invalid content type. Expected str when 'toml' is False and dict when 'toml' is True."
            )


def delete_file(path: Path) -> None:
    os.remove(path)
