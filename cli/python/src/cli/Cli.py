from pathlib import Path

class Cli:
    def __init__(self) -> None:
        print("CLI cwd:", Path.cwd())

    def run(self):
        pass
