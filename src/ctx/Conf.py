import yaml
from pathlib import Path
from pydantic import BaseModel

class Conf(BaseModel):
    name: str
    version: str
    build: list[str]
    source: str
    packages: list[str]

    @staticmethod
    def create(conf_file: Path):
        data: dict

        if not conf_file.exists():
            raise FileNotFoundError(conf_file)

        with open(conf_file, "r") as fp:
            data = yaml.safe_load(fp)

        return Conf(**data)
