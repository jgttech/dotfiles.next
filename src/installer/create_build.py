from sys import platform
from pathlib import Path
from src.os import Build
from src.env import env

def create_build() -> None:
    build = Build()
    os_packages: list[Path] = []
    os_path = Path(build.home) / "os"
    platform_path = os_path / platform
    shared_path = os_path / "shared"
    export = lambda k, v: f"export {k}=\"{v}\"\n"
    zsh_path: Path | str = ""

    if not os_path.exists():
        raise FileNotFoundError(os_path)
        
    if not shared_path.exists():
        raise FileNotFoundError(shared_path)

    if not platform_path.exists():
        raise FileNotFoundError(platform_path)

    for dir in shared_path.iterdir():
        if dir.name == "zsh":
            zsh_path = dir

        os_packages.append(dir)

    for dir in platform_path.iterdir():
        os_packages.append(dir)

    build.os = os_packages

    with open(env.build_file, "w") as file:
        file.write(build.to_json())

    zshrc_dotfiles = env.cfg / ".zshrc.dotfiles"

    with open(zshrc_dotfiles, "w") as file:
        if isinstance(zsh_path, Path):
            zsh_path = zsh_path / "main.zsh"

        file.writelines([
            "#!/usr/bin/env zsh\n",
            export("DOTFILES_BUILD_JSON", Path.home() / env.build_file.name),
            export("DOTFILES_ZSH", zsh_path),
            export("DOTFILES_BIN", env.bin),
            export("DOTFILES_HOME", env.home),
        ])
