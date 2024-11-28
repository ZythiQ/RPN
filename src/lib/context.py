from lib.expression import Expression

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
        if (exp := self.stack.pop()):
            exp.evaluate()

    def push(self, exp:Expression):
        '''Push the expression onto the stack.'''
        self.stack.append(exp)

    def touch(self, exp:Expression):
        '''Push the expression into the hand.'''
        self.hand.append(exp)

    def take(self):
        '''Pop the expression currently in the hand.'''
        return self.hand.pop()

    def bind(self, key:str, exp:Expression=None):
        '''Bind the expression to the key. Unbind if no expression.'''
        if exp: self.binds.update(key, exp)
        else: self.binds.pop(key)

    def __str__(self) -> str:
        '''Represent the current context as a string.'''
        return f'[{self.stack}]({self.hand})<{self.binds}>'
