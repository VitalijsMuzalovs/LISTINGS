# Popen()

import os
fd='GFC.txt'

file=open(fd,'w')
file.write('sveiks!')
file.close()
file.open(fd,'r')
text=file.read()
print(text)

file=os.popen(fd,'w')
file.write('asjdhask')