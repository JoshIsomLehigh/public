
"""
Generates valid 5-letter English words from the letters in a name
"""

from itertools import permutations
from english_words import english_words_set


def whats_in_your_name(your_name):
    ''' Generates all valid 5-letter English words from the letters in a name'''
    your_name = your_name.lower()
    word_list = list()
    for perm in permutations(your_name, 5):
        test_word = ''.join(perm)
        if test_word in english_words_set:
            word_list.append(test_word)
    word_list = set(word_list)
    return word_list

MY_WORD_LIST = whats_in_your_name("Alexander Isom")
print(MY_WORD_LIST)
