import tkinter as tk
from tkinter.colorchooser import askcolor

def cmdChoose():
    krasa=askcolor(title="Title")
    print(krasa)
    pass

win=tk.Tk()

tk.Button(win,text='Choose color',bg='white',command=cmdChoose).pack(side=tk.LEFT,padx=3,pady=3)


win.mainloop()