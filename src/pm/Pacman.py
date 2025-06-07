from subprocess import call
from .PackageManager import PackageManager

class Pacman(PackageManager):
    def install(self, name: str) -> None:
        call(f"sudo pacman -S --noconfirm {name} &> /dev/null", shell=True)
