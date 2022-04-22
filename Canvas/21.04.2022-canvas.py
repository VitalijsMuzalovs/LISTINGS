from tkinter import *

top=Tk()
zim=Canvas(top,bg="blue",height=250,width=300)

dati=10,20,240,210

dala=zim.create_arc(dati,start=0,fill="green",extent=150)

zim.pack()
top.mainloop()