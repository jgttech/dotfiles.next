from shutil import which
from .instance import pacman, brew

class Package:
    name: str = ""

    def __init__(self, name: str) -> None:
        self.name = name

    def exists(self) -> bool:
        return which(self.name) is not None

    def install(self) -> None:
        if pacman is not None:
            pacman.install(self.name)
        elif brew is not None:
            brew.install(self.name)
