import tkinter as tk
from tkinter import Button, ttk


def tirs():
    saraksts.set('')

def funkcija(*arg):
    ttk.Label(logs, text="index..."+str(saraksts.current())+"ir" +" "+str(n.get())).pack()
    
logs=tk.Tk()
logs.title("Izkrītošais saraksts")
logs.geometry('500x250')

#ttk.Label(logs, text="Izvēlies mēnesi!", font=('Time New Roman', 10)).grid(column=0,
#          row=0, padx=10, pady=25)

banka=('Janvāris', 'Februāris', 'Marts',  'Aprīlis')
# veidosim Combobox
n=tk.StringVar()
saraksts=ttk.Combobox(logs, width=27, textvariable=n)
saraksts['value']=banka
saraksts['state']="readonly"
saraksts.pack(padx=5, pady=5)

poga=Button(logs, text='tīrīt', command=tirs)
poga.pack()


# izsekot mainīgo ....

n.trace('w', funkcija)
#banka.current()
logs.mainloop()