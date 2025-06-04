from pathlib import Path

class FileNotFound(Exception):
    def __init__(self, file: Path | str) -> None:
        super().__init__(f"File not found: '{file}'")
