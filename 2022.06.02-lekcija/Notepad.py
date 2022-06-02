from tkinter import*

def btSave():
    global myFileName,myText
    myFileName=e.get()
    myText=textArea.get(0.0,END)
    with open(myFileName+'.txt','w',encoding='utf-8') as f:
        f.write(myText)
        f.close()
    # print(myText)
    return 0

win=Tk()
win.geometry("600x500")
win.title("TK")

saraksts=Menu(win)
win.config(menu=saraksts)
fileMenu = Menu(saraksts)
saraksts.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Exit',command=win.quit)

label=Label(win,text='Ievadi faila nosaukumu!')
label.pack(anchor="n")

e = Entry(win,width=22,font=("Arial Black",10),borderwidth=1)
e.pack(anchor="w")

bt=Button(win,text="Saglabāt datus",padx=2,pady=2,command=btSave)
bt.pack(anchor="s")

textArea = Text(win,width=30,height=25,relief="sunken")
textArea.pack(anchor="n")

win.mainloop()