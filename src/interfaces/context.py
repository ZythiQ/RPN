from interfaces.expression import Expression
from collections import deque

class Context():
    '''Maintain and execute the program.'''

    # ===== Methods ===== #
    def __init__(self, program:list[Expression], log:bool=False):
        '''Context constructor.'''
        self.stack = deque()
        self.binds = dict()
        self.hand = deque()
        self.log = log

        self.stack.extendleft(program)

    def step(self):
        '''Execute the next step.'''
        pass

    def push(self, exp:Expression):
        '''Push the expression onto the stack.'''
        pass

    def touch(self, exp:Expression):
        '''Push the expression into program hand.'''
        pass

    def bind(self, exp:Expression, key:str=None):
        '''Bind the expression to the key. Unbind if no key.'''
        pass

    def __str__(self) -> str:
        '''Represent the current context as a string.'''
        pass
