from subprocess import call
from pathlib import Path
from src.os import is_installed

p10k = Path.home() / "p10k.zsh"

if not p10k.exists() and not is_installed("p10k"):
    call("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \"$HOME/.oh-my-zsh/custom/themes/powerlevel10k\"", shell=True)
