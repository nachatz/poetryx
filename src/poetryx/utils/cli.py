import subprocess
from typing import List

def run_cli_command(commands: List[str]) -> str:
    result = subprocess.run(commands, capture_output=True, text=True)
    output = result.stdout
    return output