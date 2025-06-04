from pathlib import Path
from src.cli import Cli

if __name__ == "__main__":
    cli = Cli(Path.cwd() / "cli")
    cli.run()
