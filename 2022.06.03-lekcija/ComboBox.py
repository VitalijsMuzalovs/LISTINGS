from tkinter import *
from tkinter.ttk import Combobox 
from tkinter import messagebox
 
def retrieve():
    messagebox.showinfo(title="Choice", message="You choice is:" + n.get())

def cmdClear():
    cmb.set('')

def funkcija(*arg):
    Label(root,text='index: ' + str(cmb.current()) + ' ir' + ' ' + str(n.get())).grid(row=4,column=2)

root = Tk()
root.title('Combobox')
root.geometry("300x300")

label = Label(root,text = "Izvēlies mēnesi:").grid(row=1,column=1,padx=10,pady=25)  

n=StringVar()   

cmb = Combobox(root,height=50,textvariable=n)  
cmb['values'] = ('January', 'February', 'March',
                'April','May','June',
                'July','August','September',
                'October','November','December')
cmb.grid(row=1,column=2)
 
bttn = Button(root, text = "Tīrīt", command = cmdClear)
bttn.grid(row=2,column=2)

n.trace('w',funkcija)
    
root.mainloop()  