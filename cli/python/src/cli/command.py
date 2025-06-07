import click
from typing import Callable, TypeVar
from pathlib import Path
from os.path import join
from src.cfg import Context

T = TypeVar("T")

def command(name: str):
    cli = Path(join("cmds", name))
    ctx = Context()

    def decoractor(fn: Callable[[Context], T]) -> Callable[[], T]:
        @click.command(cli.name)
        def wrapper() -> T:
            return fn(ctx)

        return wrapper
    return decoractor
