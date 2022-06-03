from tkinter import *
from tkinter import messagebox

# Slider


def cmShow(a):
    lb.config(text='Value: '+ str(var.get()))
    return 0

def cmdShowMsg():
    messagebox.showinfo(title="Choice", message="You choice is:" + str(var.get()))


win=Tk()
win.geometry("100x200")
win.title("Mans logs")

var=DoubleVar()

skala=Scale(win,from_=0,to=100,variable=var,orient="vertical",showvalue=False,tickinterval=100,resolution=1,command=cmShow)
skala.pack()

lb=Label(win,text="Value: ")
lb.pack()

bt = Button(text="Izvelēties!",command=cmdShowMsg)
bt.pack()

win.mainloop()