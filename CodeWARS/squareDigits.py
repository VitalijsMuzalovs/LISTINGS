"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""

def square_digits(num):
    arr = str(num)
    a = [pow(int(x),2) for x in arr]
    a = ''.join(str(x) for x in a)
    return int(a)
print(square_digits(9119))