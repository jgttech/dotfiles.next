from pathlib import Path

class Environment:
    # The home/root/base directory of the
    # dotfiles.
    home: Path

    # Name of the config file at the root.
    conf_file: Path

    def __init__(self) -> None:
        self.home = Path.cwd()
        self.conf_file = self.home / "dotfiles.yml"

env = Environment()
