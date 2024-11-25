from interfaces.context import Context
from abc import ABC, abstractmethod
from typing import Any

class Expression(ABC):
    '''Abstract expression.'''

    @abstractmethod
    def evaluate(self, context:Context, log:bool=None):
        '''Evaluate the expression given the context (optionally log evaluation).'''
        pass

    @abstractmethod
    def __str__(self):
        '''Return a string representation of the expression.'''
        pass

class Literal(Expression):
    '''Abstract literal that stores its original representation.'''

    @property
    @abstractmethod
    def value(self) -> Any:
        '''Get the expression's representation.'''
        pass

    @value.setter
    @abstractmethod
    def value(self, value: Any):
        '''Set the expression's representation.'''
        pass
