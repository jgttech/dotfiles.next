from src.os import installed
from .Package import Package
from .source.File import File
from .source.Brew import Brew
from .source.Pacman import Pacman

class PackageManager:
    packages: list[Package] = []
    source: None | File | Brew | Pacman = None

    def __init__(self) -> None:
        if installed("pacman"):
            self.source = Pacman()
        elif installed("brew"):
            self.source = Brew()
        else:
            self.source = File()

    def add(self, name: str) -> None:
        self.packages.append(Package(name))

    def install(self) -> None:
        pass
