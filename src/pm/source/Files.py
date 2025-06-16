from pathlib import Path
from importlib import import_module
from src.pm.Source import Source
from src.env import env
from src.conf import conf

class Files(Source):
    def install(self, packages: list[str]) -> None:
        packages = sorted(packages)

        for dir in conf.source.iterdir():
            print(dir)

        # print("FILES:")
        # print(f"packages: {packages}")
        # print("DONE")

        # for package in packages:
        #     pkg = Path(package)
        #     module = pkg.relative_to(env.home)
        #     name = f"{module.parent / module.stem}".replace("/", ".")
        #
        #     if pkg.exists():
        #         import_module(name)
