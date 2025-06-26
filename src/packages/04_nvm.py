from subprocess import call
from pathlib import Path
from src.os import is_installed

nvm = Path.home() / ".nvm"

if not nvm.exists() and not is_installed("nvm"):
    call("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash", shell=True)
