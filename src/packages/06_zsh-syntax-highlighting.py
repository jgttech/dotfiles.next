from subprocess import call
from pathlib import Path

plugin = Path.home() / ".oh-my-zsh" / "custom" / "plugins" / "zsh-syntax-highlighting"

if not plugin.exists():
    call("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting", shell=True)
