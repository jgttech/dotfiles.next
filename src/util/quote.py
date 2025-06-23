import shlex
from pathlib import Path

def quote(arg: Path) -> str:
    return shlex.quote(str(arg))
