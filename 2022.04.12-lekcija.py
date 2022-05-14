##### LISTS #####

# Print SUM of even digits numbers , if all are EVEN
# Else -> no print

"""sum=0

for a in [2,4,6,8]:
    sum+=a
    if a%2==1:
        break
else:
    print(sum)

print("Something!")"""

#======================

"""sum = 0
for i in range(10,40):
    if i%10!=0:
        continue
    sum+=i
    print(i)
print(sum)"""

#======================

"""lst = [5,6,8,"Hi",[7,9,'text'],0.9999]
print(lst)
print(lst[1])
print(lst[4][2])
lst[2]=11
print(lst)"""

# Create an empty LIST
# lst=[]
# lst=list()

#===========
#Copying

# 1. list() function
# 2. intervāla operators "SLICES"

"""import copy
aa=[1,2,3,4,5,6]
bb=list(aa) #1. list() function
cc=aa[:] # slice
dd=copy.deepcopy(aa)
ee=aa
aa[2]=999
print(aa)
print(bb)
print(cc)
print("?>>>",ee)"""

#=============
# List comprehension

"""a=[(i+1)**2 for i in range(10)]
print(a)"""

# ACCESS to LIST
# 1. By index
# 2. By slice [start:end:step]

"""lst = [1,2,3,4,5,6]
for i in lst:
    i+=10
    print(i)"""

# change list by editing it by indexes + enumerate
"""lst = [1,2,3,4,5,6]

for i,a in enumerate(lst):
    lst[i]+=10
    print(i,a)"""

# Vertību pārbaude (in, not in)
"""aa=[1,2,3,4,5]
print(2 in aa)
print(22 in aa)
print(2 not in aa)
print(22 not in aa)"""

# List ReDim
"""lst = [1,2,3,4,5]
print(lst)
lst.append("a")
print(lst)
lst.insert(0,"bb")
print(lst)
rem = lst.pop(5) #elementa izmēšana pēc pozīcijas... ifpop()-> poped last element
print(rem)
lst.remove("a")
print(lst)
lst.insert(3,"inserted_id3")
print(lst)
del lst[0:5:2] #can delete by position,slice (slice + step)
print(lst)"""

# OOP
# Kas ir objekts, funkcija, metode, klase?
# Algoritmi - darbības un dati
# klase un objekti

# Class - local variables and functions collected (stored) in same place

"""class Car:
    # define method set name and prodYear
    def set(self,name,prodYear):
        self.name = name
        self.prodYear = prodYear
    #define method for data output
    def output(self):
        print(self.name,self.prodYear)

x = Car()   # object is created
x.set("VW",2015)
x.output()"""

from tkinter import *


logs=Tk()
logs.title("Form name")
logs.iconbitmap('E:/TEHNIKUMS/Python/img/ProductIcon.ico')
bt = Button(logs,text="Button",bg="green",fg="white")
bt.pack()
logs.mainloop()