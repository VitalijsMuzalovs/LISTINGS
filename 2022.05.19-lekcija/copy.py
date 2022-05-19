# copy - piešķīršana,seklā kopēšana, dzīļa kopēšana

# piešķīršana
"""
aa=[1,2,3]
bb=aa
print(aa,bb)
print(bb==aa,bb is aa)

aa[1]=99
print(aa,bb)
print(bb==aa,bb is aa)
"""
# seklā kopēšana - shallow copying
"""
a=[1,2,3]
b=list(a)
b2=a[:]
b3=a.copy()
b4=a[2:]
print(a,b,b2,b3,b4)
print(a is b,a is b2,a is b3,a is b4)
"""

# deep copy
import copy
a=[1,2,[4,5,6]]
b=copy. deepcopy(a)
a[1]=22
a[2][1]=55
print(b)
print(bb==aa,bb is aa)