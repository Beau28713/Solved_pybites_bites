from functools import wraps
from typing import Callable


def make_html(tag: str):
    
    def tag_wrapper(func: Callable[..., str]):
        
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            

            text = func(*args, **kwargs)

            return f"<{tag}>{text}</{tag}>"

        return wrapper

    return tag_wrapper