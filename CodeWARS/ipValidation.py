"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:
Examples of valid inputs:
1.2.3.4
123.45.67.89
Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string
"""

from ast import Bytes


def is_valid_IP(strng):
    try:
        validIP = False
        arr = strng.split('.')

        if len(arr)==4:
            for x in  arr:
                if int(x) < 256 and int(x) >= 0 and  len(x)==len(str(int(x))): 
                    validIP=True
                else:
                    validIP = False
                    break
            return print(validIP)
        else:
            return print(False)
    except:
        return print(False)

is_valid_IP('12.255.56.1')
is_valid_IP('12.255.2a0.1')
is_valid_IP('12.255.1')
is_valid_IP('')
is_valid_IP('123.456.789.0')
is_valid_IP('12.34.56 .1')
is_valid_IP('123.045.067.089')