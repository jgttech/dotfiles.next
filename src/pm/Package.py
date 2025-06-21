from pathlib import Path
from src.env import env


class Package:
    name: str
    module: None | Path = None

    def __init__(self, name: str) -> None:
        self.name = name

        if "@" in name:
            pkg, ctx = name.split("@")
            ctx_path = env.home / ctx

            self.name = pkg

            if ctx_path.is_dir():
                for module in ctx_path.iterdir():
                    if pkg in str(module) and not module.is_dir():
                        self.module = module
                        break

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, Package):
            if value.module is not None or self.module is not None:
                return self.name == value.name and self.module == value.module
            else:
                return self.name == value.name
        else:
            return False

