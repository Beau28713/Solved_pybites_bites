import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    # TODO: your code
    pp = pprint.PrettyPrinter(depth=2, width=60, sort_dicts=True )

    return pp.pformat(obj)