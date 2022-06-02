from tkinter import*

def cmdPrint():
    return 0

def btStart():
    global punkti,num,txtInput

    if num==question_count:
        lb2.pack_forget()
        txtInput.pack_forget()
        bt['text']=f'Punkti {punkti}\n Klikšķis , lai aizvērtu logu'
        bt['command']=beigas()
        bt.pack()
        return
    
    if num==0:
        check()
    txtInput.delete("1.0",END)
    txtInput.insert('1.0',fileContent[num][0]) 
    bt.pack_forget() 
    num+=1  
    win.geometry('500x300')
    
    return 0

def check():
    global punkti
    if atbilde.get()==fileContent[num-1][1]:
        txtInput.insert(END,"Pareizi")
        punkti+=1
    else:
        txtInput.insert(END,"Nepareizi")
    atbilde.set("")
    btStart()

def beigas():
    win.destroy()

def atbildes_logs():
    global txtInput
    txtInput=Entry(win,textvariable=atbilde)
    txtInput.pack()
    txtInput.bind("<Return",lambda x: check())

fileContent=[
    ("Q1","1"),
    ("Q2","2"),
    ("Q3","3"),
]

question_count = len(fileContent)
punkti=0
num=0


win=Tk()
win.geometry("500x500")
win.title("Uzdevums")

atbilde=StringVar()
var2=StringVar()


lb=Label(win,width=30,height=2,bg="orange",font=("Arial Black",16),text="Pārbaudījums")
lb.pack()

lb2 = Label(win,width=22,bg="cyan",fg="black",font=("Arial Black",12),borderwidth=1,text="Press START to begin!") 
lb2.pack(anchor="n")

txtInput = Text(win,width=22,height=2,bg="green",fg="yellow",font=("Arial Black",12),borderwidth=1) 
txtInput.insert('1.0',lb2)
txtInput.pack()

bt=Button(win,text="Start!",padx=2,pady=2,command=btStart)
bt.pack(anchor="s")

win.mainloop()