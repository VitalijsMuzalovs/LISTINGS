# Gadu skaitītājs

import datetime
import tkinter as tk



Logs=tk.Tk()
Logs.geometry("620x780")
Logs.title(" Vecuma kalkulatos App ")
name = tk.Label(text = "Vārds")
name.grid(column=0,row=1)
year = tk.Label(text = "Gads")
year.grid(column=0,row=2)
month = tk.Label(text = "Mēnesis")
month.grid(column=0,row=3)
date = tk.Label(text = "Diena")
date.grid(column=0,row=4)
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)
def getInput():
    name=nameEntry.get()
    m = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    
    textArea =tk.Text(Logs,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = " Hei {m}!!!. Tev ir {age} gadi! ".format(m=name, age=m.age())
    textArea.insert(tk.END,answer)


button=tk.Button(Logs,text="Rēķināt",command=getInput,bg="pink")
button.grid(column=1,row=5)





class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age

Logs.mainloop()