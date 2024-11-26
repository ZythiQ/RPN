from interfaces.context import Context
from abc import ABC, abstractmethod

class Expression(ABC):
    '''Abstract expression (smallest unit of logic).'''

    def __init__(self, value):
        '''Expression constructor.'''
        self._value = value

    def set_value(self, value):
        '''Set the value for the expression.'''
        self._value = value

    def get_value(self):
        '''Get the value of the expression.'''
        return self._value

    @abstractmethod
    def evaluate(self, context:Context, log:bool=None):
        '''Evaluate the expression given the context (optionally log evaluation).'''
        pass
