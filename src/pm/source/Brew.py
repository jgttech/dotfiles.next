import json
from subprocess import run, call
from src.pm.Source import Source


class Brew(Source):
    def install(self, packages: list[str]) -> None:
        casks = []
        formulae = []

        for package in packages:
            proc = run(
                ["brew", "info", "--json=v2", package],
                capture_output=True,
                text=True,
                check=False,
            )

            if proc.returncode == 0:
                data = json.loads(proc.stdout)

                if data.get("formulae") and len(data["formulae"]) > 0:
                    formulae.append(package)
                elif data.get("casks") and len(data["casks"]) > 0:
                    casks.append(package)

        if len(formulae) > 0:
            call(f"brew install {" ".join(formulae)}", shell=True)

        if len(casks) > 0:
            call(f"brew install --cask {" ".join(casks)}", shell=True)
