from os import getcwd, chdir, environ, getenv, path
from pathlib import Path
from inspect import cleandoc
from subprocess import run
from src.sys import quote
import src.cli as cli

@cli.installer("python")
def install(ctx: cli.Context) -> None:
    bin = Path(ctx.build.bin)
    entry = bin / "dotfiles"
    cli = Path(ctx.build.cli)
    home = getenv("HOME", "")
    vars = {
        "cli": f"~{str(cli)[len(home):]}" if home in str(cli) else cli
    }

    wd = getcwd()
    try:
        chdir(cli)

        env = environ.copy()
        env["UV_CACHE_DIR"] = quote(cli / ".uv-cache")

        sync = run(["uv", "sync", "--no-config"], env=env, check=True).returncode

        if sync != 0:
            raise RuntimeError(f"Failed to sync project: {cli}")
    finally:
        chdir(wd)

    # The code that gets output within
    # the bin directory.
    script = cleandoc("""
        #!/usr/bin/env bash
        uv run --directory {cli} --project {cli} main.py $@
    """.format(**vars).strip())

    entry.touch()
    entry.write_text(script, encoding="utf-8")
    entry.chmod(0o777)
