from abc import abstractmethod
from typing import TypeVar
from BabelFish.output import Output

V = TypeVar('V')

class ValueOutput(Output[V]):
    def __init__(self, value: V = None):
        super().__init__(value, None)
