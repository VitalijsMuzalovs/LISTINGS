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
    with open(fileDir,'r',errors='ignore') as file:
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
        

# print(movableBrandSet)
all_Lists=[]

for b_num,brand in enumerate(movableBrandSet):
    globals()['%s' % brand+'_List']=[]
    # print(['%s' % brand+'_List'])
    for pos in movablePrice:
        if brand in movablePrice[pos]['brand']:
            globals()['%s' % brand+'_List'].append([pos,movablePrice[pos]['price_ref'],movablePrice[pos]['price_1'],movablePrice[pos]['price_2'],movablePrice[pos]['price_3'],movablePrice[pos]['price_4'],movablePrice[pos]['price_5'],movablePrice[pos]['price_6'],movablePrice[pos]['price_7']])
    # all_Lists.append(['%s' % brand+'_List'])
    all_Lists.append(['%s' % brand+'_List'])



# for n,(key, value) in enumerate(movablePrice.items()):
#     print(n,key, value)
# print('='*30)

def plot(brand_List,brand_name):
    plt.subplots(figsize=(15,6))
    x=range(0,len(brand_List[0])-1)
    plt.title(brand_name.split("'")[1].split("_")[0])
    myNp=np.array(brand_List)
    a=myNp[myNp[:, 1].argsort()]

    for i in myNp:
        # print(i)
        z=i[1:]
        y = [float(el) for el in z]
        plt.plot(x,y,label=i[0])
        
    plt.legend()
    plt.show()

ok=True

while ok:
    print('='*35)
    for num,lists in enumerate(all_Lists):
        listName = str(lists).split("'")[1].split('_')[0]
        
        print(num,listName)
    print('='*35)
    brand_num = input('Please,select a brand number: ')
    if brand_num=='stop': 
        break
    else:
        brand_num=int(brand_num)
        list_name = str(all_Lists[brand_num])
        # print(f'You are selected {list_name}')
        # print(all_Lists[brand_num])

        plot(globals()['%s' % str(all_Lists[brand_num]).split("'")[1]],list_name)