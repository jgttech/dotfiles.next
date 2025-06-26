from subprocess import call
from src.pm.source import Brew
from src.os import is_installed

packages = ["go", "odin", "zig", "rust", "lua", "luarocks", "terraform"]
brew = Brew()
bin = Brew.bin()

if bin is not None:
    dir = bin.parent
    pkgs = []

    for pkg in packages:
        if not (dir / pkg).exists() or not is_installed(pkg):
            status = call(f"{bin} list | grep {pkg} &> /dev/null", shell=True)

            if status == 1:
                if pkg == "terraform":
                    call(f"{bin} tap hashicorp/tap", shell=True)
                    call(f"{bin} install hashicorp/tap/terraform", shell=True)
                else:
                    pkgs.append(pkg)

    if len(pkgs) > 0:
        brew.install(pkgs)
