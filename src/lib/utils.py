
def assertType(obj, expType, typeName=None):
    '''Assert that the object is of the expected type. Otherwise raise a TypeError.'''
    if not isinstance(obj, expType):
        # Multiple or single type?
        if not isinstance(expType, type):
            expected = ' or '.join(t.__name__ for t in expType)
        else: expected = typeName or expType.__name__
            
        raise TypeError(f'{type(obj).__name__} "{obj}" must be of type {expected}.')

    
def assertChar(obj):
    '''Assert the object is a Character.'''
    assertType(obj, str)

    if len(obj) != 1:
        raise ValueError(f'"{obj}" must be a single character.')