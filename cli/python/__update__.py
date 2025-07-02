from os import chdir, environ, getcwd
from pathlib import Path
from subprocess import run
from src.util import quote
import src.cli as cli

@cli.update("python")
def main(ctx: cli.Context) -> None:
    env, _ = ctx.state
    cli = env.source
    uv = Path.home() / ".local" / "bin" / "uv"

    wd = getcwd()
    try:
        chdir(cli)

        ENV = environ.copy()
        ENV["UV_CACHE_DIR"] = quote(cli / ".uv-cache")

        sync = run(
            [str(uv), "sync", "--no-config", "--upgrade"],
            env=ENV,
            check=True,
        )

        if sync.returncode != 0:
            raise RuntimeError(f"Failed to sync project: {cli}")
    finally:
        chdir(wd)
