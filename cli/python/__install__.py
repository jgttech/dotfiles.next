from os import chdir, environ, getcwd
from subprocess import run
from inspect import cleandoc
from src.util import quote
import src.cli as cli

@cli.install("python")
def main(ctx: cli.Context) -> None:
    env, _ = ctx.state
    cli = env.source

    wd = getcwd()
    try:
        chdir(cli)

        ENV = environ.copy()
        ENV["UV_CACHE_DIR"] = quote(cli / ".uv-cache")

        sync = run(["uv", "sync", "--no-config"], env=ENV, check=True)

        if sync.returncode != 0:
            raise RuntimeError(f"Failed to sync project: {cli}")
    finally:
        chdir(wd)

    entry = env.bin / "dotfiles"

    # The code that gets output within
    # the bin directory.
    script = cleandoc("""
        #!/usr/bin/env bash
        uv run --directory {src} --project {src} main.py $@
    """.format(**{
        "src": str(env.source),
    }).strip())

    entry.touch()
    entry.write_text(script, encoding="utf-8")
    entry.chmod(0o777)
