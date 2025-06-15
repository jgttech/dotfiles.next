import click
from click import Context
from typing import Callable, TypeVar
from src.env import env
from src.conf import conf
from src.pm import PackageManager

T = TypeVar("T")

def command(dir: str):
    cli = env.home / "cli" / dir
    package_manager = PackageManager()

    for package in conf.packages:
        package_manager.add(package)

    package_manager.install()

    def decorator(fn: Callable[[Context], T]) -> Callable[[], T]:
        @click.command(cli.name)
        @click.pass_context
        def wrapper(ctx) -> T:
            return fn(ctx)

        return wrapper
    return decorator
