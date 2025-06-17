from pathlib import Path
from src.conf import conf


class Package:
    name: str
    module: None | Path = None

    def __init__(self, name: str) -> None:
        self.name = name

        if "@" in name:
            pkg, ctx = name.split("@")
            self.name = pkg

            if ctx == "local":
                for asset in conf.local.iterdir():
                    if not asset.is_dir() and pkg in str(asset):
                        self.module = asset

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, Package):
            return self.name == value.name
        else:
            return False

