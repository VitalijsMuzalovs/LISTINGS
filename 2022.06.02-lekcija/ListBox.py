from msilib.schema import ListBox
from tkinter import*

# Slider

def cmdPrint():
    # e.config(text=lstBox.curselection())
    vert=lstBox.get(lstBox.curselection())
    var1.set(vert)
    return 0

    

win=Tk()
win.geometry("300x300")
win.title("Saraksta izveide")

var1=StringVar()
# var2=StringVar()
# var2.set((1,2,3,4))

e = Label(win,width=22,bg="green",fg="yellow",font=("Arial Black",12),borderwidth=1,textvariable=var1 )
e.pack(anchor="n")

bt=Button(win,text="Print selection",padx=2,pady=2,command=cmdPrint)
bt.pack(anchor="s")

lstBox = Listbox(win,height=50,width=30) #,listvariable=var2)

# option 1
myList=[101,102,103,104]

for k in myList:
    lstBox.insert('end',k)

# option 2
# lstBox.insert(1,"1")  
# lstBox.insert(2, "first")  
# lstBox.insert(3, "2")  
# lstBox.insert(4, "3")
# lstBox.insert(5, "4")  
# lstBox.insert(6, "11")
# lstBox.insert(7, "22")
# lstBox.insert(8, "33")
# lstBox.insert(9, "44")  

lstBox.delete(0)
   
lstBox.pack()  

win.mainloop()