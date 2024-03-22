from typing import TypeVar
from BabelFish.output import Output

V = TypeVar('V')

class ErrorOutput(Output[V]):
    def __init__(self, error = None, value: V = None):
        super().__init__(value, error)

    def is_error(self) -> bool:
        return True