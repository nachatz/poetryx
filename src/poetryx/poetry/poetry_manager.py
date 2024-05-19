from poetryx.utils.cli import run_cli_command

class PoetryManager:
    def get_virtualenv_path(self) -> str:
        path = run_cli_command(["poetry", "env", "info", "-p"])
        
        if path:
            return path
        else:
            raise ValueError("Unable to find virtualenv path")
       
