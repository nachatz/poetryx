from abc import ABC, abstractmethod

class SettingsManager(ABC):
    """Abstract class for managing settings in an IDE."""
    
    @abstractmethod
    def set_poetry_debugger(self, path: str) -> None:
        pass
