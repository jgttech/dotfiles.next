from subprocess import call
from pathlib import Path

nvm = Path.home() / ".nvm"

if nvm.exists():
    call("source ~/.nvm/nvm.sh; nvm install --lts; nvm use --lts --default && npm i -g npm && npm i -g yarn && npm i -g pnpm", shell=True)
