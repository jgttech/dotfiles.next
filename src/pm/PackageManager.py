from src.os import installed
from .Package import Package
from .source.Files import Files
from .source.Brew import Brew
from .source.Pacman import Pacman

class PackageManager:
    packages: list[Package] = []
    source: None | Brew | Pacman = None
    files = Files()

    def __init__(self) -> None:
        if installed("pacman"):
            self.source = Pacman()
        elif installed("brew"):
            self.source = Brew()

    def add(self, name: str) -> None:
        dep = Package(name)

        if not len([pkg for pkg in self.packages if pkg == dep]):
            self.packages.append(dep)

    def install(self) -> None:
        packages = [p.name for p in self.packages if p.module is None]
        modules = [str(p.module) for p in self.packages if p.module is not None]

        if len(modules) > 0:
            self.files.install(modules)

        if self.source is not None:
            self.source.install(packages)
