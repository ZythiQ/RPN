from interfaces.expression import Expression
from interfaces.context import Context
import pkgutil, importlib, inspect

class Parser():
    '''Static script parser.'''

    # ===== Constants ===== #
    EXPS_PKG = 'expressions'
    EXPS:list = []

    # ===== Loaders ===== #
    @staticmethod
    def __load_expressions():
        '''Dynamically load expressions.'''

        # If not init:
        if not Parser.EXPS:
            for _, name, _ in pkgutil.iter_modules([Parser.EXPS_PKG]):
                module = importlib.import_module(f'{Parser.EXPS_PKG}.{name}')

                # Append expression if valid:
                for _, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, Expression):
                        Parser.EXPS.append(obj)

    # ===== Methods ===== #
    @staticmethod
    def validate(script:str) -> bool:
        '''Validate the script syntax and return result.'''
        pass

    @staticmethod
    def parse(script:str) -> Context | None:
        '''Parse the script and return a context. None if invalid.'''
        pass

    @staticmethod
    def parseFile(absolutePath:str) -> Context | None:
        '''Parse the script file and return a context. None if invalid.'''
        pass
