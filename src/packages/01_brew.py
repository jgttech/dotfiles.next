from subprocess import call
from src.pm.source import Brew

bin = Brew.bin()

if bin is not None and not bin.exists():
    call("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"", shell=True)
