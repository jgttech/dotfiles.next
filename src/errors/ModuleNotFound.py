class ModuleNotFound(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"Module not found: '{name}'")
