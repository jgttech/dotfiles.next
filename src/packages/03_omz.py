from subprocess import call
from pathlib import Path
from src.os import is_installed

omz = Path.home() / ".oh-my-zsh"

if not omz.exists() and not is_installed("omz"):
    call("sh -c \"$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\"", shell=True)
