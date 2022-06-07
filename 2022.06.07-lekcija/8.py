# izveidot dialoga logu, kas pec ievaditiem datiem nosaka cilvēka vecumu

from tkinter import *
import datetime

def cmdCalc():
    myName=txtName.get()
    m=Person(myName,datetime.date(int(txtYear.get()),int(txtMonth.get()),int(txtDay.get())))    
    atbilde='Hi,{m}! Tev ir {age}'.format(m=myName,age=m.age)
    txtArea.insert(atbilde,END)

win=Tk()
win.title('Vecums')
win.geometry('400x400')

lbName=Label(win,width=30,text='Name:').grid(row=1,column=1)
txtName=Entry(win,width=30).grid(row=1,column=2)

lbYear=Label(win,width=30,text='Year:').grid(row=2,column=1)
txtYear=Entry(win,width=30).grid(row=2,column=2)

lbMonth=Label(win,width=30,text='Month:').grid(row=3,column=1)
txtMonth=Entry(win,width=30).grid(row=3,column=2)

lbDay=Label(win,width=30,text='Day:').grid(row=4,column=1)
txtDay=Entry(win,width=30).grid(row=4,column=2)

bt=Button(win,text='Submit',command=cmdCalc).grid(row=5,column=2)
txtArea=Text(win,width=30,height=10).grid(row=6,column=2)

class Person:
    def __init__(self):
        self.name=name
        self.birthdate=birthdate

    def age(self):
        today=datetime.date.today()
        age=today.year-self.birthdate.year
        return age


win.mainloop()