__author__ = 'Kalyan'

notes = '''
1. Read instructions for each function carefully.
2. Try to use builtins and data structures instead of writing your own.
3. If something about the function spec is not clear, use the corresponding test
   for clarification
'''
from placeholders import *
import string

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists, only use string functions
# assume words are separated by spaces. you can use control flow statements
def prune_either_or(sentence):
    i=sentence.find('either')
    j=sentence.find('or')
    if i==-1 or j== -1:
        return sentence
    else:
       return sentence[:i]+sentence[i+len('either')+1:j-1]
    pass

# Create a palindrome of twice the length of the word passed in.
# e.g. app -> appppa, bat -> battab etc.
# hint: look up extended slice notation.
def create_palindrome(word):
    if word==None:
        return word
    else:
        return word+word[len(word)::-1]
    pass

import string


# returns a dict which maps a -> 1, b -> 2 ... z->26 and A -> 1, B ->2 ... Z->26
# no control flow allowed.
def get_encoding_dict():
    return dict(zip(string.letters, range(1, 27)*2))


def test_either_or_pruning():
    assert "We can go to a movie" == prune_either_or("We can either go to a movie or a hotel")
    assert "We can go either way" == prune_either_or("We can go either way")
    assert "" == prune_either_or("either or")
    assert "either way is fine" == prune_either_or("either way is fine")

def test_create_palindrome():
    assert "battab" == create_palindrome("bat")
    assert "abba" == create_palindrome("ab")
    assert "" ==create_palindrome("")
    assert None == create_palindrome(None)

def test_get_encoding_dict():
    d = get_encoding_dict()
    assert len(d) == 52
    for key in d:
        assert ord(key.lower()) - ord('a') + 1 == d[key]

three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___
