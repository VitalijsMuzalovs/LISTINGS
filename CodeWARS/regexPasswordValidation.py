"""
You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a digit
only contains alphanumeric characters (note that '_' is not alphanumeric)
"""
import re

def out(txt):
    # return re.findall("[0-9a-zA-Z]{1}",txt) and re.search("[.]{6}",txt)
    # return re.match("[0-9a-zA-Z]{6}",txt) and re.findall("[0-9a-zA-Z]{1}",txt)
    return re.match("([0-9a-zA-Z]{6})([0-9a-zA-Z]{1})",txt) 
    # return re.findall("alnum:",txt)

print(out('fjd3IR9'))
print(out('a123456;89'))