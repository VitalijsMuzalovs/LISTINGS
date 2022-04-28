# 1.uzd
# Creating passwords - GENERATE
# bez dublētaām rakstazīīmēm
"""
import random

s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
skaits=8
parole="".join(random.sample(s,skaits))

print(parole)
"""

# 2.uzd
# Creating passwords - GENERATE
# bez dublētaām rakstazīīmēm - 2.variants
"""
import random
import string


def parole(size=8,chars=string.ascii_letters+string.digits+string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

print(parole(int(input('Cik simboli būs parolē?'))))
"""

# 3.uzd
# resize image
"""
import PIL
import os
import os.path
from PIL import Image

f=r"E:\TEHNIKUMS\Python\images"
for file in os.listdir(f):
    f_img=f+"\\"+file
    img=Image.open(f_img)
    img=img.resize((150,150))
    img.save(f_img)
"""

# 4.uzd
# parbaudīt , vai sarakstā ir konkretais saraksts un noteikt tā indeksu
"""
lst=[44,2,13,52,802,44]

def meklet0(x):
    if x in lst:
        return "OK"
    else:
        return "FAIL"

def meklet1(x):
    for i in range(len(lst)):
        if lst[i]==x:
            return "Meklētā skaitļa indekss ir: "+str(i)
    else:
        return "Tāda skaitļa nav!"
    return 0

print(meklet1(52))
"""

#  5.uzd
# Function 1: .format()
"""
print("{:,.2f}".format(6.5892))

a="{:e}".format(9.045612121331254)
print(a)

a="{:_}".format(45612121331254)   # 1000 devider
print(a)
"""

# 6.uzd
# .join() ir noderīga virknes metode
"""
lst=["Ziema","Pavasaris","Vasara"]
a="/".join(lst)
print(a)

print("x".join("Sveiki"))
"""

#  7.uzd
# split
"""
adrese = "cape@inbox.lv"
a = list((adrese.split("@")))
print (a[0])
"""

#  8.uzd
# .strip
"""
str1 = "  asd addd"
# print(str1.strip())
print(str1.strip("d")) # lstrip/rstrip
"""

#  9.uzd
# REQUEST (Data request and reply between Client-Server; for HTTP/HTTPS)
"""
import requests

f=r"https://www.grobinasskola.lv"
data=requests.get(f) # response server ->> 200 -> ok
data=data.text
print(data) """

#  10.uzd
"""
import pandas as pd
f=r"E:\TEHNIKUMS\Python\28.04.2022-lekcija\Sample.xlsx"
df=pd.read_excel(f,sheet_name="Sheet2")
print(df)"""

# 11.uzd
# READ CSV
"""
import pandas as pd
f=r"E:\TEHNIKUMS\Python\28.04.2022-lekcija\Sample.csv"
file=open(f,"r")
df=file.read()
print(df)
"""

# 13.uzd
# csv.reader
import pandas as pd
import csv
f=r"E:\TEHNIKUMS\Python\28.04.2022-lekcija\Sample.csv"
file=open(f,"r")
data=csv.reader(file,delimiter=' ')
for i in data:
    print (i)