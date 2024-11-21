from collections import deque
from interfaces.expression import Expression

class Context():
    '''Maintain and execute the program.'''

    # ===== Attributes ===== #
    program:list[Expression]
    memory:deque
    binds:dict
    hand:deque
    log:bool

    # ===== Methods ===== #
    def __init__(self, program:list[Expression], log:bool=False):
        '''Context constructor.'''
        self.program = program
        self.memory = deque()
        self.binds = dict()
        self.hand = deque()
        self.log = log

    def execute(self):
        '''Execute the program.'''
        pass

    def touch(self, exp:Expression):
        '''Push the expression into program hand.'''
        pass

    def queue(self, exp:Expression):
        '''Queue the expression into program memory.'''
        pass

    def bind(self, exp:Expression, key:str=None):
        '''Bind the expression to the key. Unbind if no key.'''
        pass

    # ===== Dunders ===== #
    def __str__(self) -> str:
        '''Represent the current context as a string.'''
        pass
