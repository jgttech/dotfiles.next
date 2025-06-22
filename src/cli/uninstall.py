import click
from typing import Callable, TypeVar
from src.env import env
from .pass_context import pass_context
from .Context import Context
from .MODE import MODE

T = TypeVar("T")

def uninstall(dir: str):
    def decorator(fn: Callable[[Context], T]) -> Callable[[], T]:
        @click.command(dir)
        @pass_context
        def wrapper(ctx: Context, *args, **kwargs):
            env.mode = MODE.UNINSTALL
            return fn(ctx, *args, **kwargs)
        return wrapper
    return decorator
