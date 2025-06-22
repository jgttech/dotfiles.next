import click
from typing import Callable, TypeVar
from src.pm import PackageManager
from src.env import env
from src.conf import conf
from .pass_context import pass_context
from .Context import Context
from .MODE import MODE

T = TypeVar("T")

def install(dir: str):
    def decorator(fn: Callable[[Context], T]) -> Callable[[], T]:
        @click.command(dir)
        @pass_context
        def wrapper(ctx: Context, *args, **kwargs):
            env.mode = MODE.INSTALL
            package_manager = PackageManager()

            for package in conf.packages:
                package_manager.add(package)

            package_manager.install()

            if not env.bin.exists():
                env.bin.mkdir(parents=True)

            if not env.cfg.exists():
                env.cfg.mkdir(parents=True)

            return fn(ctx, *args, **kwargs)
        return wrapper
    return decorator

