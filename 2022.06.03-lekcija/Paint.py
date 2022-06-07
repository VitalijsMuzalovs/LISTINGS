from tkinter import *
from tkinter.colorchooser import askcolor
from unittest.mock import DEFAULT

class zimet(object):
    DEFAULT_PEN_SIZE=5.0
    DEFAULT_COLOR="black"

    def __init__(self):
        self.win=Tk()
        self.win.geometry('500x550')

        # Pen button
        self.pen_poga=Button(self.win,text='Pen',command=self.btPen)
        self.pen_poga.grid(row=0,column=0)

        # Colorchooser button
        self.chColorBt=Button(self.win,text='Color',command=self.chooseColor)
        self.chColorBt.grid(row=0,column=1)

        # Paint area
        self.c=Canvas(self.win,bg='white',width=500,height=500)
        self.c.grid(row=1,columnspan=5)

        self.win.mainloop()

    def btPen(self):
        self.active_button(self.pen_poga)

    def chooseColor(self):
        self.active_button(self.chColorBt)

    def active_button(self,):
        pass

    def paint(self,event):
        pass


        


if __name__=='__main__':
    zimet()
