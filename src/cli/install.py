import click
from typing import Callable, TypeVar
import src.installer as installer
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

            installer.setup()
            installer.install_packages()
            installer.create_build()
            installer.create_backup()
            installer.create_links()

            return fn(ctx, *args, **kwargs)
        return wrapper
    return decorator
