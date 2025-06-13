from pathlib import Path
from .Conf import Conf

class Environment:
    # Name of the config file at the root.
    conf_file: Path

    # The config file data.
    conf: Conf

    @staticmethod
    def create():
        cwd = Path.cwd()
        env = Environment()

        env.conf_file = cwd / "dotfiles.yml"
        env.conf = Conf.create(env.conf_file)

        return env

env = Environment.create()
