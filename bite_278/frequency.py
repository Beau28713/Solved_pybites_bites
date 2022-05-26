"""You are given a list of integers. Write code to find the majority and minorty numbers in that list.

Definition: a majority number is the one appearing most frequently, a minority number appears least frequently.

Here is a simple example how it should work:
"""

from collections import Counter

def major_n_minor(numbers):
    return Counter(numbers).most_common(1)[0][0], Counter(numbers).most_common()[-1][0]