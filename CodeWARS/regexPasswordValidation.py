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
    return re.match(r"[\da-zA-Z]{6}",txt)

print(out('fjd3IR9'))
print(out('123abc'))