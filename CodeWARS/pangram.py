"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation."""
import re

def is_pangram(s):
    s = s.replace(" ", "").lower()
    s = re.sub(r'[^a-zA-Z]', '', s)
    alphabet_len = 26
    set_len = len(set(s))
    # print(set(s))
    # print(set_len,alphabet_len)
    if set_len==alphabet_len: 
        return True
    else:
        return False
    
print(is_pangram("The quick brown fox jumps over the lazy dog"))