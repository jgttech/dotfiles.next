from dataclasses_json import DataClassJsonMixin
from dataclasses import dataclass, field
from pathlib import Path
from json import load
from src.env import DOTFILES_CONFIG_JSON
from src.errors import FileNotFound

@dataclass
class ProjectJson(DataClassJsonMixin):
    version: str = ""
    out: str = ""
    cfg: str = ""
    bin: str = ""
    dependencies: list[str] = field(default_factory=list)

    @staticmethod
    def load(dir: Path):
        file = dir / DOTFILES_CONFIG_JSON

        if not file.exists():
            raise FileNotFound(file)

        with open(file, "r") as ref:
            return ProjectJson.from_dict(load(ref))
