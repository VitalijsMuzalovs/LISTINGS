import matplotlib.pyplot as plt
import numpy as np

xx=[]
yy=[]

with open('2022.05.31-lekcija\data.txt','r') as f:
    for line in f:
        row = line.split(';')
        xx.append(int(row[0]))
        yy.append(int(row[1]))
f.close

z=['Pirmdiena','Otrdiena','Trešdiena','Ceturtdiena','Piektdiena']

# print(xx)
# print(yy)

x = np.arange(len(z))  # the label locations
width = 0.35  # the width of the bars
# print(x)

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, xx, width, label='Vīrieši')
rects2 = ax.bar(x + width/2, yy, width, label='Sievietes')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Daudzums')
ax.set_title('Rīgas klubu apmeklētāji')
ax.set_xticks(x, z)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
