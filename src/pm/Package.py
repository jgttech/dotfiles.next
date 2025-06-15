from pathlib import Path
from src.conf import conf


class Package:
    name: str
    module: None | Path = None

    def __init__(self, name: str) -> None:
        if "@" in name:
            pkg_name, dir = name.split("@")
            self.module = conf.source / dir / f"{pkg_name}.py"
            self.name = pkg_name
        else:
            self.name = name
