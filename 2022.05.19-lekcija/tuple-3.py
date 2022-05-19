#Tuple - unpacking

"""
saraksts=(10,20,30,40)
a,b,c,d,=saraksts
print(a)
# pāršķiršana

s1=(11,22)
s2=(99,88)

s1,s2=s2,s1
print(s1)
print(s2)
"""
#kopēt elementu 44 un 55
saraksts=(11,22,33,44,55,66)
# new=(saraksts[3],saraksts[4]) #1.var
new=(saraksts[3:-1])
print(new)