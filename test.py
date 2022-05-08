def mfn(x):
    return x

a=[1,2,3,4,5,6,7]
b=[7,6,5,4,3,2,1,0]
C=zip(a,b)
# print(list(C))

print(type(C))

result = map(lambda x, y: x+y, a,b)
print(set(result))
