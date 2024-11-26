from interfaces.expression import Expression
from interfaces.context import Context
from collections import namedtuple

class Parser():
    '''Parses a script and returns a program context.'''

    # ===== Other ===== #
    Container = namedtuple('Container', ['expression', 'rightKey', 'strict'])

    # ===== Methods ===== #
    def __init__(self):
        '''Parser constructor.'''
        self.default = None
        self.expressions = dict()

    def addDefault(self, exp:Expression):
        '''Add a default for unknown bindings.'''
        pass

    def addExpression(self, exp:Expression, key:str, rightKey:str=None, strict:bool=True):
        '''Add a key-bound expression (default strict syntax).'''
        pass

    def parse(self, script:str) -> Context | None:
        '''Parse the script and return a context. None if invalid.'''
        pass

    def parseFile(self, absolutePath:str) -> Context | None:
        '''Parse the script file and return a context. None if invalid.'''
        pass
