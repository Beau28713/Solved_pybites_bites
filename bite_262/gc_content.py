"""Example:
DNA Sequence:
AAAAAAAATTTTTTGGGGCC
A=8, T=6, G=4, C=2, TOTAL = 20
GC content = n(G|C) / n(A|C|G|T) = 6/20 = 3/10 => 30%
"""
from collections import Counter

def calculate_gc_content(sequence):
    sequence = sequence.upper()
    count = Counter(sequence)
    n1 = count["G"] + count["C"]
    n2 = count["A"] + count["C"] + count["G"] + count["T"]
    gc_content = (n1 / n2) * 100
    print(count)
    # return round(gc_content, 2)
    