"""Our 4th test Bite. Michael made a calculator that will be able to accept a list 
of decimal digits and returns an integer where each int of the given list represents 
decimal place values from first element to last.
He wrote the function in such a way that it only accepts positive digits in range(0, 10) 
and anything that is not raises a ValueError if its out of range, or a TypeError if its not an int type.

Some examples:

[0, 4, 2, 8] => 428
[1, 2] => 12
[3] => 3
[6, 2, True] => raises TypeError
[-3, 12] => raises ValueError
[3.6, 4, 1] => raises TypeError
['4', 5, 3, 1] => raises TypeError
In this Bite you are tasked to write the tests for this function. Good luck and keep calm and code in Python!
"""


import pytest

from numbers_to_dec import list_to_decimal

@pytest.mark.parametrize("test_input, expected", 
                        [([0,1,2,3], 123), 
                        ([3,1,5], 315),
                        ([9, 7], 97),
                        ([9], 9)])
def test_list_to_decimal_1(test_input, expected):
    assert list_to_decimal(test_input) == expected

@pytest.mark.parametrize("test_input", [[-1,2,14], [10]])
def test_list_to_decimal_2(test_input):
    with pytest.raises(ValueError):
        list_to_decimal(test_input)

@pytest.mark.parametrize("test_input",[[8.3, 8, 6], [True, 9, 6]])
def test_list_to_decimal_3(test_input):
    with pytest.raises(TypeError):
        list_to_decimal(test_input)
