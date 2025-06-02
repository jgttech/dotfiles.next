class FileNotFound(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(f"File not found: {msg}")
