from tkinter import *
from tkinter.ttk import Combobox 
from tkinter import messagebox
 
def retrieve():
    messagebox.showinfo(title="Choice", message="You choice is:" + n.get())

def cmdClear():
    cmb.set('')


def funkcija(*arg):
    az=Label(root,text='index: ' + str(cmb.current()) + ' ir' + ' ' + str(n.get()))
    lbList.append(az)
    az.pack()
    #print(lbList)

def cmdDelete():
    for i in lbList:
        i.after(5, i.destroy())

root = Tk()
root.title('Combobox')
root.geometry("300x300")

label = Label(root,text = "Izvēlies mēnesi:").pack()  

lbList=[]

n=StringVar()   

cmb = Combobox(root,height=50,textvariable=n)  
cmb['values'] = ('January', 'February', 'March',
                'April','May','June',
                'July','August','September',
                'October','November','December')
cmb.pack()
 
bttn = Button(root, text = "Tīrīt", command = cmdClear)
bttn.pack()

btDel = Button(root, text = "DELETE", command = cmdDelete)
btDel.pack()


n.trace('w',funkcija)

# cmb.bind('<<ComboboxSelected>>', funkcija)
    
root.mainloop()  