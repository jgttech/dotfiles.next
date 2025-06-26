import click
from os import rename
from sys import platform
from subprocess import call
from typing import Callable, TypeVar
from pathlib import Path
from src.os import Build
from src.pm import PackageManager
from src.conf import conf
from src.env import env
from .pass_context import pass_context
from .Context import Context

T = TypeVar("T")

def install(dir: str):
    def decorator(fn: Callable[[Context], T]) -> Callable[[], T]:
        @click.command(dir)
        @pass_context
        def wrapper(ctx: Context, *args, **kwargs):
            env.source = env.home / "cli" / dir
            HOME = Path.home()

            # Setup for the build.
            bin = env.bin
            cfg = env.cfg

            if not bin.exists():
                bin.mkdir(parents=True)

            if not cfg.exists():
                cfg.mkdir(parents=True)

            # Install the packages.
            package_manager = PackageManager()

            for package in conf.packages:
                package_manager.add(package)

            package_manager.install()

            # Generate the build
            build = Build()
            os_packages: list[Path] = []
            os_path = Path(build.home) / "os"
            platform_path = os_path / platform
            shared_path = os_path / "shared"
            export = lambda k, v: f"export {k}=\"{v}\"\n"

            if not os_path.exists():
                raise FileNotFoundError(os_path)

            if not shared_path.exists():
                raise FileNotFoundError(shared_path)

            if not platform_path.exists():
                raise FileNotFoundError(platform_path)

            for d in shared_path.iterdir():
                os_packages.append(d)

            for d in platform_path.iterdir():
                os_packages.append(d)

            build.lang = build.source.stem
            build.os = os_packages

            with open(env.build_file, "w") as file:
                file.write(build.to_json())

            zshrc_dotfiles = env.cfg / ".zshrc.dotfiles"

            with open(zshrc_dotfiles, "w") as file:
                file.writelines([
                    "#!/usr/bin/env zsh\n",
                    export("DOTFILES_BUILD_JSON", HOME / env.build_file.name),
                    export("DOTFILES_ZSH_MAIN", HOME / ".config/zsh/main.zsh"),
                    export("DOTFILES_ZSH_DIR", HOME / ".config/zsh"),
                    export("DOTFILES_BIN", env.bin),
                    export("DOTFILES_HOME", env.home),
                ])

            # Do any backup work I need.
            build = Build()
            zshrc = HOME / ".zshrc"
            zshrc_backup = HOME / build.zshrc_backup

            if zshrc.exists():
                rename(zshrc, zshrc_backup)

            # Create the links for everything.
            cwd = env.cfg.parent
            dirs: set[Path] = set[Path]()

            for link in build.os:
                dirs.add(link.parent)

            for d in dirs:
                stow: list[str] = [f"stow -t {HOME}"]

                for sub in d.iterdir():
                    stow.append(sub.name)

                call(" ".join(stow), shell=True, cwd=d)

            call(f"stow -t {HOME} {env.cfg.name}", shell=True, cwd=cwd)

            return fn(ctx, *args, **kwargs)
        return wrapper
    return decorator
