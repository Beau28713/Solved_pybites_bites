"""In this Bite you'll learn to catch and raise Python exceptions.

Write a simple division function meeting the following requirements:

1. When the denominator is zero, catch the corresponding exception and return zero.

2. When the numerator or denominator have an invalid type reraise the corresponding exception.

3. If the result of the division is negative raise a ValueError.

Check the tests if you have questions about what your code needs to pass. Have fun!
"""

def positive_divide(numerator, denominator):
    try:
        if denominator == 0:
            return 0

        elif denominator / numerator < 0:
            raise ValueError

        return numerator/denominator

    except TypeError:
        raise TypeError
