"""In this Bite you will swap case all pybites characters (both lower- and upper case) for a given text.

Not much more as for our instruction, just complete convert_pybites_chars

(Note that all converted chars are in the string pybites)
"""

PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    new = ""

    for char in text:
        if char.lower() in PYBITES:
            new += (char.swapcase())
        else:
            new += (char)
        
    return new