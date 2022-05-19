# Dictionaries

vards=['viens','divi','trīs']
vertibas=[1,2,3]

# myDict={i:j for i,j in zip(vards,vertibas)} #my variant
# myDict=dict(zip(vards,vertibas)) #1.st variant

myDict=dict() # myDict={}
for i in range(len(vards)):
    myDict.update({vards[i]:vertibas[i]})

print(myDict)