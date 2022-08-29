"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""

from queue import Empty


def increment_string(strng):
    num = ''.join(x for x in strng if x.isnumeric())
    count = len(num)
    chars = ''.join(x for x in strng if x.isalpha())
    if len(str(num)) == 0:
        return chars+str(1)
    else: 
        num= int(num)+1
        zeroes = '0' * (count - len(str(num)))
        return chars + zeroes + str(num)

print(increment_string(""))