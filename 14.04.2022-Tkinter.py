from tkinter import *
from tkinter import messagebox
from tkinter import font

logs=Tk()
logs.title("Form name")
logs.iconbitmap('E:/TEHNIKUMS/Python/img/ProductIcon.ico')
logs.geometry("400x200")

def btClick():
    messagebox.showwarning("Warning!","Warning message")
    return 0
def closeWin():
    logs.destroy()
    return 0
def delText():
    inp.delete(0,END)
    return 0
def showInfo():
    messagebox.showinfo("Info","Shown INFO!")
    return 0

bt = Button(logs,text="Button",bg="green",fg="white",padx=20,pady=10,command=lambda:btClick())
bt2 = Button(logs,text="Close",bg="red",fg="white",padx=20,pady=10,command=lambda:closeWin())
bt3 = Button(logs,text="Clear",bg="brown",fg="white",padx=20,pady=10,command=lambda:delText())

bt4 = Button(logs,text="INFO",bg="blue",fg="white",padx=20,pady=10,command=lambda:showInfo())

inp = Entry(logs,font=("Arial black",22))

bt.grid(row=0,column=0)
bt2.grid(row=0,column=2)
inp.grid(row=1,column=0,columnspan=4)
bt3.grid(row=0,column=1)
bt4.grid(row=2,column=0)

# bt.pack() #-i-1#
logs.mainloop()

#-i-1-# PACK vietā pogam izmanto režģi (grid) 0.rinda un 0.kolonna