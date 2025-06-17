from subprocess import call
from src.pm.Source import Source


class Pacman(Source):
    def install(self, packages: list[str]) -> None:
        cmd = ["sudo pacman -S --noconfirm"]

        for package in packages:
            cmd.append(package)

        call(" ".join(cmd), shell=True)
