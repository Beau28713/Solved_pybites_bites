VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    for letter in input_str.lower():
        if letter  not in VOWELS:
            return False
        else:
            answer = True

    return answer

def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    for char in input_str.lower():
        x = PYTHON.find(char)
        if x >= 0:
            return True
        

def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    for char in input_str:
        if char.isdigit():
            return True