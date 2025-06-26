from subprocess import call, run
from src.pm.Source import Source


class Pacman(Source):
    def install(self, packages: list[str]) -> None:
        pkgs = []

        for package in packages:
            pkgs.append(package)

        cmd = run(["sudo", "pacman", "-Qi", *pkgs], capture_output=True, text=True)
        stderr: list[str] = list(filter(lambda txt: bool(txt.strip()), cmd.stderr.split("\n")))

        if len(stderr) > 0:
            pkgs = []

        for line in stderr:
            if "was not found" in line:
                pkg = line.split(" ")[2].replace("'", "")
                pkgs.append(pkg)

        if len(pkgs) > 0:
            call(" ".join(["sudo pacman -S --noconfirm", *pkgs]), shell=True)
