import yaml
from pathlib import Path
from src.os import Package

class Conf:
    name: str = ""
    version: str = ""
    build: list[str] = []
    source: Path
    packages: list[Package] = []

    @staticmethod
    def create(file: Path, home: Path):
        data: dict
        conf = Conf()

        if not file.exists():
            raise FileNotFoundError(file)

        with open(file, "r") as fp:
            data = yaml.safe_load(fp)
            source = home / data["source"]

            conf.name = data["name"]
            conf.version = data["version"]
            conf.build = data["build"]
            conf.source = source

            for pkg in data["packages"]:
                conf.packages.append(Package(pkg, source, home))

        return conf
