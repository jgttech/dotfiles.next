from .create_decorator import create_decorator
from .MODE import MODE

def install(dir: str):
    return create_decorator(MODE.INSTALL, dir)
    # cli = env.home / "cli" / dir
    #
    # def decorator(fn: Callable[[Context], T]) -> Callable[[], T]:
    #     @click.command(cli.name)
    #     @pass_context
    #     def wrapper(ctx: Context, *args, **kwargs):
    #         package_manager = PackageManager()
    #
    #         for package in conf.packages:
    #             package_manager.add(package)
    #
    #         package_manager.install()
    #
    #         if not env.bin.exists():
    #             env.bin.mkdir(parents=True)
    #
    #         if not env.cfg.exists():
    #             env.cfg.mkdir(parents=True)
    #
    #         return fn(ctx, *args, **kwargs)
    #     return wrapper
    # return decorator
