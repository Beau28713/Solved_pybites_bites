def countdown():
    """Write a generator that counts from 100 to 1"""
    num = 100
    while num > 0:
        yield num
        num -= 1