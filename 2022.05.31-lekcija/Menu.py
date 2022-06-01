from cProfile import label
from tkinter import*

def komanda():
    return 0


win=Tk()
win.title("Tulkotājs")
win.geometry('500x200')

saraksts=Menu(win)
win.config(menu=saraksts)

# create MenuList

fileMenu = Menu(saraksts)
editMenu = Menu(saraksts)

saraksts.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='New',command=komanda)
fileMenu.add_command(label='Exit',command=win.quit)

saraksts.add_cascade(label='Edit',menu=editMenu)
editMenu.add_radiobutton('Lat')

win.mainloop()