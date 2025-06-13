from pydantic import BaseModel
from src.pm import File, Pacman, Homebrew

class Package(BaseModel):
    name: str
    installer: File | Pacman | Homebrew
