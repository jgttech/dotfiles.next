import json
from sys import platform
from pathlib import Path
from subprocess import run, call
from src.pm.Source import Source


class Brew(Source):
    @staticmethod
    def bin() -> Path | None:
        if platform == "linux":
            return Path("/home/linuxbrew/.linuxbrew/bin/brew")
        elif platform == "darwin":
            return Path("/usr/local/bin/brew")

        return None

    def install(self, packages: list[str]) -> None:
        brew = str(Brew.bin() or "brew")
        casks = []
        formulae = []

        for package in packages:
            proc = run(
                [brew, "info", "--json=v2", package],
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
            cmd = f"{brew} install {" ".join(formulae)}"
            print(cmd)
            call(cmd, shell=True)

        if len(casks) > 0:
            cmd = f"{brew} install --cask {" ".join(casks)}"
            print(cmd)
            call(cmd, shell=True)
