"""There are three tasks to complete for this Bite:

Finish the function load_words which creates and returns a list of words from a text file.
Finish the function calc_word_value which calculates and returns a word's Scrabble value.
Finish the function max_word_value which finds and returns the dictionary word with the highest score.
Notes:

The text of the dictionary is downloaded for you and is available with the path contained in the variable DICTIONARY.
The words in the file are separated by a newline character.
Letters not found in LETTER_SCORES score zero points.
Look at the TESTS tab to see what your code needs to pass. Enjoy!
"""

import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, "r") as file:
        dic_list = [x.strip() for x in file]
    
    return dic_list


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    score = 0
    for letter in word.upper():
        if letter in LETTER_SCORES.keys():
            score += LETTER_SCORES.get(letter)
    return score


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    max_dic = {}
    for word in words:
        max_word = calc_word_value(word)
        max_dic.update({word: max_word})
    
    return max(max_dic, key=max_dic.get)