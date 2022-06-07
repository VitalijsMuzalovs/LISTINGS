#IOError
import os

try:
    filename='GFC.txt'
    f=open(filename,'r')
    text=f.read()
    f.close

except IOError:
    print('No such file: '+filename)