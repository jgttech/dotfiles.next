from dynamic_yaml import load
from pathlib import Path
from src.env import env

class Conf:
    name: str = ""
    version: str = ""
    local: Path
    packages: list[str] = []

    def __init__(self) -> None:
        file = env.conf_file
        home = env.home

        if not file.exists():
            raise FileNotFoundError(file)

        with open(file, "r") as ref:
            data = load(ref)

            for package in data["packages"]:
                self.packages.append(package)

            self.name = data["name"]
            self.version = data["version"]
            self.local = home / data["local"]

conf = Conf()
