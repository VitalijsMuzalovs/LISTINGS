from tkinter import*
from gtts import gTTS
import os

def translate():
    teksts=e.get()
    mm=var.get()

    if mm==1:
        valoda='lv'
    else:
        valoda='en'
    
    speak=gTTS(teksts,lang=valoda,slow=False)
    speak.save('translate.mp3')
    os.system('translate.mp3')

    return 0


win=Tk()
win.title("Tulkotājs")

var= IntVar()

label=Label(win,text='Ievadi tekstu, kurš jāatsaņo!')
label.pack()
e = Entry(win,width=15,font=("Arial Black",22),borderwidth=4)
e.pack()
bt=Button(win,text="TRANSLATE",padx=10,pady=10,command=translate)
bt.pack()
opt_1= Radiobutton(win,text='Latviešu',value=1,variable=var)
opt_2= Radiobutton(win,text='Angļu',value=2,variable=var)
opt_1.pack()
opt_2.pack()

win.mainloop()