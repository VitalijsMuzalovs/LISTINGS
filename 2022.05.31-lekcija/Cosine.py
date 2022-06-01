from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0.0,5.0,100)
y= np.cos(2*np.pi*x)*np.exp(-x)

top=0.5
bottom=-0.5

font={'family':'serif',
    'color':'blue',
    'weight':'normal',
    'size':16}

plt.plot(x,y,color='black')
plt.xlabel('Laiks (s)',fontdict=font)
plt.ylabel('Spriegums (mV)',fontdict=font)
plt.title('Amortizēta ekspponenciālā samazināšanās',fontdict=font)

plt.text(3,0.50,r'$\cos(2\pi t) \exp(-t)$',fontdict=font)

plt.subplots_adjust(left=0.15)

plt.legend()
plt.show()
