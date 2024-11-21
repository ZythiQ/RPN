from abc import ABC, abstractmethod
from interfaces.context import Context

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
