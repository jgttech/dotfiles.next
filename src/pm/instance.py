from shutil import which
from .Homebrew import Homebrew
from .Pacman import Pacman

# Singleton instances for package management.
pacman = Pacman() if which("pacman") is not None else None
brew = Homebrew() if which("brew") is not None else None
