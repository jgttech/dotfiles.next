from typing import Tuple
from src.env import Environment, env
from src.conf import Conf, conf

class Context:
    @property
    def state(self) -> Tuple[Environment, Conf]:
        return (env, conf)
