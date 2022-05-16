from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt

fileDir="2022.04.22-RD_parser\RDveikals-Fridges\Fridges_REF.txt" #REFERENCE FILE
mypath='2022.04.22-RD_parser\RDveikals-Fridges'

brand=[]
model=[]
price=[]
ref={}

def getRefLists(fileDir):
    with open(fileDir,'r') as file:
        for line in file:
            # print(line)
            tmp=line.split(' ')
            tmp=[el for el in tmp if el]
            brand.append(tmp[1])

            price.append(tmp[-2])
            model.append((' '.join(tmp[2:-2]))[:-1])
    return model,brand,price

model,brand,price=getRefLists(fileDir)
for n in range(len(brand)):
    # print(f'{brand[n]} - {model[n]} - {price[n]}')
    ref[model[n]]={'brand':brand[n],'price_ref':price[n]}
    # print(ref)

onlyfiles = [f for f in listdir(mypath)]
myFileList=[]
for file in onlyfiles:
    if file[-4:]=='.txt' and file[:-4].split('-')[-1].isdigit():
        myFileList.append(mypath+'\\'+file)

# print(myFileList)

key_nr=1

for dir in myFileList:
    price_nr = 'price_'+str(key_nr)
    model,brand,price=getRefLists(dir)
    for num,n in enumerate(model):
        if n in ref:
            ref[n][price_nr]=price[num]
    key_nr+=1

movablePrice={}
movableBrandSet=set()
for el in ref:
    if ref[el]['price_1']!=ref[el]['price_4']: 
        movablePrice[el]=ref[el]
        # print(ref[el]['brand'])
        movableBrandSet.add(str(ref[el]['brand']))
        

print(len(movableBrandSet))
# for k in movableBrandSet:
#     print(ref.keys(k))
for n,(key, value) in enumerate(movablePrice.items()):
    print(n,key, value)
print('='*30)