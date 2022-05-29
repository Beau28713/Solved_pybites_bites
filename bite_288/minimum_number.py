"""Write a function that accepts a list of digits and returns the smallest number that can be created by combining unique digits.

Therefore, you have to ignore duplicated digits.  

Examples:  

[1] => 1

[7, 1] => 17  

[1, 9, 5, 9, 1] => 159

Note: An empty input list [] should return 0.
"""

from typing import List
from itertools import combinations


def minimum_number(digits: List[int]) -> int:
    none_dup = list(set(digits))
    none_dup.sort()
    comb = list(combinations(none_dup, len(none_dup)))
    g =""
    if len(none_dup) <= 0:
        return 0
    else:
        for x in comb[0]:
            if x == 0 and len(none_dup) > 1:
                continue
            else:
                g += "".join(str(x))

    return int(g)