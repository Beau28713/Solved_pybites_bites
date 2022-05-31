from fizzbuzz import fizzbuzz
import pytest

@pytest.mark.parametrize("test_input, expected", 
                        [(0, "Fizz Buzz"), (1, 1), (2, 2), 
                        (3, "Fizz"), (5, "Buzz"), (6, "Fizz"), 
                        (7, 7), (8, 8), (9, "Fizz"), (15, "Fizz Buzz")])
def test_fizzbuz(test_input, expected):
    assert fizzbuzz(test_input) == expected