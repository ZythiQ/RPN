from interfaces.expression import Literal
from interfaces.context import Context

class Pack(Literal):
    '''Literal implementation; contains one or more characters.'''

    # ===== Properties ===== #
    @property
    def value(self) -> list[str]:
        '''Get the pack's representation.'''
        return self._values

    @value.setter
    def value(self, values:list[str]):
        '''Set the pack's representation.'''
        if not all(isinstance(v, str) and 1 == len(v) for v in values):
                raise ValueError('All values must be single characters.')
        
        self._values = list(values)

    # ===== Methods ===== #
    def __init__(self, *values: str):
        '''Pack constructor.'''
        self.value(values)

    def evaluate(self, context:Context, log:bool=None):
        '''Pushes itself to the hand.'''
        context.touch(self)

    def __str__(self):
        '''Return a string representation of the pack.'''
        return f'{''.join(self._values)}'
