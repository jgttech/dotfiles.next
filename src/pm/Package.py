class Package:
    pass

# from pathlib import Path
# from src.pm import File, Pacman, Homebrew
# from .installed import installed
#
# class Package:
#     name: str
#     package_manager: 
#
#     def __init__(self, name: str, source: Path, home: Path) -> None:
#         self.name = name
#
#         if "@" in name:
#             pkg, path = name.split("@")
#             dir = home / source / path
#
#             self.name = pkg
#             self.package_manager = File(dir)
#         elif installed("pacman"):
#             self.package_manager = Pacman()
#         elif installed("brew"):
#             self.package_manager = Homebrew()
#
#     def install(self):
#         self.package_manager.install(self.name)
