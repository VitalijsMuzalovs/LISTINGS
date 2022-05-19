from tkinter import*
from tkinter import messagebox
import random

def uzmini(num):
    global try_count
    global text
    
    try_count-=1
    speletajs=int(e.get())

    if rand_num==speletajs:
        text.set('Tu uzvarēji!')
        e.pack_forget()
    elif try_count==0:
        text.set('Tu zaudēji!')
    elif speletajs<rand_num:
        text.set('Nepareizi,atlikuši '+ str(try_count)+' mģīnājumi,mini lielāku skaitli!')
        e.delete(0,END)
    elif speletajs>rand_num:
        text.set('Nepareizi,atlikuši '+ str(try_count)+' mģīnājumi,mini mazāku skaitli!')
        e.delete(0,END)

    # messagebox.showerror("Error!",e)
    return 0

try_count = 12
try_num=0
rand_num = random.randint(1,25)

win=Tk()
win.title("Uzmini")
label=Label(win,text='Gues a number from 1 to 25')
e = Entry(win,width=15,font=("Arial Black",22),borderwidth=4)
bt=Button(win,text="OK",padx=0,pady=0,command=lambda:uzmini(e))

text=StringVar()
text.set('Tev ir 12 mēģinājumi!')
atskaite=Label(win,textvariable=text)


label.grid(row=0,column=0,columnspan=4)
e.grid(row=1,column=0,columnspan=4)
bt.grid(row=1,column=5)
atskaite.grid(row=2,column=0,columnspan=4)
win.mainloop()