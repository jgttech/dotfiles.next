from .PackageManager import PackageManager

class Homebrew(PackageManager):
    def install(self, name: str) -> None:
        print(f"Installing package {name}")
