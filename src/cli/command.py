import click
from typing import Callable, TypeVar
from src.pm import PackageManager
from src.env import env
from src.conf import conf
from .pass_context import pass_context
from .Context import Context

T = TypeVar("T")

def command(dir: str):
    cli = env.home / "cli" / dir
    package_manager = PackageManager()

    for package in conf.packages:
        package_manager.add(package)

    package_manager.install()

    def decorator(fn: Callable[[Context], T]) -> Callable[[], T]:
        @click.command(cli.name)
        @pass_context
        def wrapper(ctx: Context, *args, **kwargs):
            return fn(ctx, *args, **kwargs)

        return wrapper
    return decorator
