import click
from typing import Callable, TypeVar
from pathlib import Path
from os.path import join
from src.cfg import Context

T = TypeVar("T")

def installer(dir: str):
    cli = Path(join("cli", dir))
    ctx = Context(Path.cwd(), cli)

    def decoractor(fn: Callable[[Context], T]) -> Callable[[], T]:
        @click.command(cli.name)
        def wrapper() -> T:
            ctx.init()
            return fn(ctx)

        return wrapper
    return decoractor
