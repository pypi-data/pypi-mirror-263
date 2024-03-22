from typing import TypeVar, Generic, Optional
from BabelFish.callback_decorator import CallbackDecorator
from BabelFish.output import Output
from BabelFish.value_out_put import ValueOutput

from BabelFish.use_case import UseCase

P = TypeVar('P')
R = TypeVar('R')

class UseCaseUnit(Generic[P, R]):
    def __init__(self, use_case: UseCase[P, R], param: Optional[P] = None):
        self.use_case = use_case
        self.param = param

    def process(self) -> Output[R]:
        callback = self.Callback()
        decorator = CallbackDecorator(self.use_case, callback.set)
        decorator.process(self.param)
        return callback.output

    class Callback:
        def __init__(self):
            self.output = ValueOutput()

        def set(self, value: Output[R]):
            self.output = value
