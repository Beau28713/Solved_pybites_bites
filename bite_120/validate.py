from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError
            elif arg < 0:
                raise ValueError
        
        return func(*args)
    return wrapper