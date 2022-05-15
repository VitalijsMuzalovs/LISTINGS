import numpy as np
import matplotlib.pyplot as plt

fileDir="2022.04.22-RD_parser\RDveikals-Fridges\Fridges_REF.txt" #REFERENCE FILE

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
    ref={model[n]:{'brand':brand[n],'price_ref':price[n]}}
    print(ref)

fileDir="2022.04.22-RD_parser\RDveikals-Fridges\Fridges13.05.2022.txt"
model,brand,price=getRefLists(fileDir)
for n in model:
    if n in ref:
        ref[n]={'price_1':price[n]}
        print(ref[n])

# for key, value in ref.items():
#     print(key, value)
#     print('='*30)

# print(ref['CU3331'])

# fig, ax = plt.subplots()
# for color in ['tab:blue', 'tab:orange', 'tab:green']:
#     n = 750
#     x, y = np.random.rand(2, n)
#     scale = 200.0 * np.random.rand(n)
#     ax.scatter(x, y, c=color, s=scale, label=color,
#                alpha=0.3, edgecolors='none')

# ax.legend()
# ax.grid(True)

# plt.show()