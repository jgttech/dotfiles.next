import json
from pathlib import Path
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
from src.env import DOTFILES_JSON
from src.errors import FileNotFound

@dataclass
class Project(DataClassJsonMixin):
    version: str = ""
    name: str = ""
    cli: str = ""
    stow: str = ""
    out: str = ""
    cfg: str = ""
    bin: str = ""

    @staticmethod
    def load(dir: Path):
        json_file = dir / DOTFILES_JSON

        if not json_file.exists():
            raise FileNotFound(str(json_file))

        with open(json_file, "r") as file:
            return Project.from_dict(json.load(file))
