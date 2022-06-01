import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0.0,2.0,0.01)
s=np.sin(2*np.pi*t)

top=0.5
bottom=-0.5

above=np.ma.masked_where(s<top,s)
below=np.ma.masked_where(s>bottom,s)
middle=np.ma.masked_where((s>top) | (s<bottom) ,s)

fig,ax=plt.subplots()
ax.plot(t,above,t,middle,t,below)
plt.show()
