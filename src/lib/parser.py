from lib.utils import assertType, assertChar
from lib.expression import Expression
from lib.context import Context

from collections import namedtuple, deque

class Parser():
    '''Parses a script and returns a program context.'''

    # ===== Other ===== #
    Binding = namedtuple('Binding', ['expression', 'rightKey', 'strict'])

    # ===== Methods ===== #
    def __init__(self):
        '''Parser constructor.'''
        self.default = None
        self.expressions = dict()

    def addDefault(self, exp:Expression):
        '''Add a default for unknown bindings.'''
        assertType(exp, Expression)
        self.default = exp

    def addExpression(self, exp:Expression, key:str, rightKey:str=None, strict:bool=True):
        '''Add a key-bound expression (default strict syntax).'''
        assertType(exp, Expression)
        assertChar(key)

        if rightKey is not None:
            assertChar(rightKey)

        self.expressions.update(key, Parser.Binding(exp, rightKey, strict))

    def parse(self, script:str) -> Context | None:
        '''Parse the script and return a context. None if invalid.'''
        if not isinstance(script, str):
            raise TypeError('Script must be a string.')

        partialExps = deque()
        partialLits = list()

        for token in script.split(''):
            # Use default if no binding:
            binding = self.expressions.get(token, Parser.Binding(self.default, None, True))
            # TODO

    def parseFile(self, absolutePath:str) -> Context | None:
        '''Parse the script file and return a context. None if invalid.'''
        pass
