import click
from click import Context
from typing import Callable, TypeVar
from src.ctx import env

T = TypeVar("T")

def command(dir: str):
    cli = env.home / "cli" / dir

    def decorator(fn: Callable[[Context], T]) -> Callable[[], T]:
        @click.command(cli.name)
        @click.pass_context
        def wrapper(ctx) -> T:
            return fn(ctx)

        return wrapper
    return decorator
