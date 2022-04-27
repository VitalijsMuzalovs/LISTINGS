# klasēm un pie objektiem
"""
Izveidot klasi ,kurā ar konstruktora init tiek definēts vārds un uzrūna
"""

"""
class Hello():
    def __init__(self,name):
        self.name = name

    def greating(self):
        print("Hello,",self.name,"!")

Hello("Jānis").greating()
"""

# optimizācija - lielam pogu skaitam
"""
from tkinter import *
from tkinter import ttk

win=Tk()
win.geometry("750x250")

txt=Entry(win,width=30,bg="white")
txt.pack(pady=10)

btList={}
dati=["Text1","Text2","Text3","Text14"]

def updTxt(text):
    txt.delete(0,END)
    txt.insert(0,text)

for i in dati:
    def likt(x=i):
        return updTxt(x)
    btList[i]=ttk.Button(win,command=likt)
    btList[i].pack()

win.mainloop()
"""

# runa ir par vienkāršu konteinera loģīku
"""
from tkinter import *
from tkinter import ttk

logs=Tk()
logs.geometry("750x250")

apg=LabelFrame(logs)
canvas=Canvas(apg)
canvas.pack(side=RIGHT,fill=BOTH,expand=1)
apg.pack(fill=BOTH,expand=1,padx=30,pady=30)

for i in range(5):
    ttk.Button(canvas,text="Podziņa "+str(i)).pack()

logs.mainloop()
"""

# izveidot 10 pogas Poga0-Poga 9 uz kuras uzklikškinot terminālā paradās Podzina0-Podzina9
"""
from tkinter import *
from tkinter import ttk

win=Tk()
win.geometry("300x300")

bt={}

def printTerminal(text):
    print("Poga "+ str(text))

for i in range(0,10):
    def likt(x=i):
        return printTerminal(x)
    bt[i]=ttk.Button(win,text="Poga "+str(i),command=likt)
    bt[i].pack()

win.mainloop()
"""
"""
import tkinter as tk

def klik(x):
    print("Poga "+str(x))

def otra():
    app=tk.Tk()
    frame=tk.Frame(app)
    frame.pack()

    buttons=[]
    for x in range(10):
        b=tk.Button(frame,text="Poga "+str(x),command=lambda:klik(buttons[x]))
        b.pack()
        buttons.append(b)

    app.mainloop()
    return 0

otra()
"""
"""
import random
import string

class Phone():
    def __init__(self,brandName,osName,id):
        self.brandName=brandName
        self.osName=osName
        self.id=id

    def __str__(self):
        return f"{self.brandName},{self.osName},{self.id}"    
    

def genID():
    return ''.join(random.choice(string.digits) for i in range(11))

phone1=Phone("Samsung","Android",genID())
phone2=Phone("Apple","iOS",genID())
print(phone1)
print(phone2)
"""

#radio pogas - option box

"""from tkinter import *
from tkinter import font
from tkinter.ttk import *

logs=Tk()
logs.geometry("175x175")

v=StringVar(logs,"1")

style=Style(logs)
style.configure("TRadiobutton",background="light green",foreground="red",font=("Arial",10,"bold"))

# jāizveido vārdnīca
values={"poga1":"1","poga2":"2","poga3":"3","poga4":"4","poga5":"5"}

for (text,value) in values.items:
    Radiobutton(logs,text=text,variable=v,value=value).pack(side=TOP,ipday=5)

logs.mainloop()"""

# Images
"""
from PIL import Image
fails=Image.open(r"E:\TEHNIKUMS\Python\Gallery\img\Logo1.jpg")
fails.show()

fails.close()
"""
# OS
"""
import os

# os.remove(r"E:\TEHNIKUMS\Python\26.04.2022-File\kaste.txt")
if os.path.exists(r"E:\TEHNIKUMS\Python\26.04.2022-File\kaste.txt"):
    os.rename(r"E:\TEHNIKUMS\Python\26.04.2022-File\kaste.txt",r"E:\TEHNIKUMS\Python\26.04.2022-File\kaaaaaste.txt")
else:
    print("File doesn't exist!")
"""

