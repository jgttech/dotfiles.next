from subprocess import call
from pathlib import Path

bun = Path.home() / ".bun"

if not bun.exists():
    call("curl -fsSL https://bun.sh/install | bash", shell=True)
