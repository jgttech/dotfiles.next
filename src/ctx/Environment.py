from pathlib import Path
from .Conf import Conf

class Environment:
    # The home/root/base directory of the
    # dotfiles.
    home: Path

    # Name of the config file at the root.
    conf_file: Path

    # The config file data.
    conf: Conf

    @staticmethod
    def create():
        cwd = Path.cwd()
        env = Environment()

        env.home = cwd
        env.conf_file = cwd / "dotfiles.yml"
        env.conf = Conf.create(file=env.conf_file, home=cwd)

        return env

env = Environment.create()
