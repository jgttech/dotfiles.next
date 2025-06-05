import json
from pathlib import Path
from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin

@dataclass
class BuildJson(DataClassJsonMixin):
    version: str = ""
    base: str = ""
    cli: str = ""
    stow: str = ""
    out: str = ""
    cfg: str = ""
    bin: str = ""
    zshrc_backup: str = ""
    created_at: int = 0
    packages: list[str] = field(default_factory=list)

    def __init__(self, dir: Path) -> None:
        super().__init__()
        print(dir)

    def save(self, to: Path) -> None:
        with open(to, "w") as file:
            file.write(json.dumps(self.to_dict(), indent=2))
