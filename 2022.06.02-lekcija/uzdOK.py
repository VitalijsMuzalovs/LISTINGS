import tkinter as tk



banka=[
      ("1.jautājums", "1"),
      ("2.jautājums", "2"),
      ("3.jautājums", "3")
]
jaut_skaits=len(banka)
punkti=0
num=0

def sakt():
    global num, punkti, ievade

    if num==jaut_skaits:
        text.pack_forget()
        ievade.pack_forget()
        poga['text']=f"Punkti {punkti}\n Klikšķis, lai aizvērtu logu"
        poga['command']=beigas
        poga.pack()
        return

    if num==0:
        # te bija kļūda
        atbildes_logs()
    logs.geometry('400x200')
#te bija kļūLuda
    text['height'] = 1
   

    text.delete("1.0", tk.END)
    text.insert('1.0', banka[num][0])
    poga.pack_forget()
    num+=1



def beigas():
    logs.destroy()


def atbildes_logs():
    global ievade
    ievade=tk.Entry(logs, textvariable=atbilde, bg="yellow", font="Arial 20")
    ievade.pack()
    ievade.bind("<Return>", lambda x: parbaud())
    ievade.focus()
 
def parbaud():
    global punkti
    if atbilde.get()==banka[num-1][1]:
        text.insert(tk.END, "Pareizi")
        punkti+=1
    else:
        text.insert(tk.END, "Nepareizi")
    atbilde.set("")
    sakt()


 
logs=tk.Tk()
label=tk.Label(logs, text="Pārbaudījums", bg='coral', font="Arial 48")
label.pack()


nosacijums="""Atbildi uz jautājumiem!

Lai sāktu spēlim klik uz START.
Tu redzēsi jautājumus.
Uzrakstot atbildi, nospiest ENTER!
"""
text=tk.Text(logs, height=12, font="Arial 20")
text.insert('1.0', nosacijums)
text.pack()

poga=tk.Button(logs, text='START', font=('Arial 20'), command=sakt)
poga.pack()

atbilde=tk.StringVar()
logs.mainloop()