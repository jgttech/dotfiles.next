import yaml
from pathlib import Path
from src.env import env

class Conf:
    name: str = ""
    version: str = ""
    build: list[str] = []
    local: Path
    packages: list[str] = []

    def __init__(self) -> None:
        file = env.conf_file
        home = env.home

        if not file.exists():
            raise FileNotFoundError(file)

        with open(file, "r") as ref:
            data = yaml.safe_load(ref)
            
            self.name = data["name"]
            self.version = data["version"]
            self.build = data["build"]
            self.packages = data["packages"]
            self.local = home / data["local"]

conf = Conf()
