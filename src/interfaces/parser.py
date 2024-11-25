from interfaces.expression import Expression, Literal
from interfaces.context import Context

class Parser():
    '''Script parser.'''

    # ===== Methods ===== #
    def __init__(self):
        '''Parser constructor.'''
        self.expressions = list()
        self.literal = None

    def validate(self, script:str) -> bool:
        '''Validate the script syntax and return result.'''
        pass

    def parse(self, script:str) -> Context | None:
        '''Parse the script and return a context. None if invalid.'''
        pass

    def parseFile(self, absolutePath:str) -> Context | None:
        '''Parse the script file and return a context. None if invalid.'''
        pass

    # ===== Loaders ===== #
    def addExpression(self, exp:Expression, key:chr):
        '''Add a key-bound expression.'''
        pass

    def addLiteral(self, lit:Literal):
        '''Add a default expression for unknown bindings.'''
        pass

    def addContainer(self, cntr:Expression, leftKey:chr, rightKey:chr, asLiterals:bool=False):
        '''Add a key-delimited container expression (optionally parse children as literals).'''
        pass
