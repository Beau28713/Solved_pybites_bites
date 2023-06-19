"""- Allowed operations are addition +, subtraction - or multiplication *.

- Result is always an int (positive or negative).

- i1, i2, i3 [...] are ints between 1 and 9 (included) but can only be used once in a solution.

Task
- Write a function that receives a list of operators & result and returns all possible solutions as a list / generator of a list of int as shown above.

- Make sure to implement the order of operations correctly (multiplication before addition or subtraction).

- Using operators other than  +, - or * should raise a ValueError.

- Using non int as a result should raise ValueError.

Good luck and keep calm and code in Python!"""

from itertools import permutations
from operator import add, sub, mul
from typing import List, Union, Iterable


def find_all_solutions(
    operator_path: List[str], expected_result: int
) -> Union[List[List[int]], Iterable[List[int]]]:
    # TODO: blank canvas to fill
    pass
