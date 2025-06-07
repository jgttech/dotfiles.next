from abc import ABC, abstractmethod

class PackageManager(ABC):
    @abstractmethod
    def install(self, name: str) -> None:
        """Should handle installing a single package."""
        pass
