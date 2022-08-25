"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
"""
import re
def alphabet_position(text):
    rez = ""
    text=text.lower()
    text = re.sub(r'[^a-z]', '', text)
    for x in text:
        rez +=str(ord(x) - 96)+' '
    print(rez)
    return rez

alphabet_position("The sunset sets at twelve o' clock")