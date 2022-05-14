import numpy as np
import matplotlib.pyplot as plt

fileDir="2022.04.22-RD_parser\RDveikals-Fridges\Fridges.txt"

brand=[]
model=[]
price=[]

with open(fileDir,'r') as file:
    for line in file:
        # print(line)
        tmp=line.split(' ')
        tmp=[el for el in tmp if el]
        brand.append(tmp[1])

        price.append(tmp[-2])
        model.append((' '.join(tmp[2:-2]))[:-1])
        
for n in range(len(brand)):
    print(f'{brand[n]} - {model[n]} - {price[n]}')



fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()