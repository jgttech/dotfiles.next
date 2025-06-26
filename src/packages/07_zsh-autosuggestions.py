from subprocess import call
from pathlib import Path

plugin = Path.home() / ".oh-my-zsh" / "custom" / "plugins" / "zsh-autosuggestions"

if not plugin.exists():
    call("git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions", shell=True)
