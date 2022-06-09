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
        self.setup()
        self.win.mainloop()



    def btPen(self):
        self.active_button(self.pen_poga)


    def chooseColor(self):
        self.ereaser_on=False
        self.color=askcolor(color=self.color)[1]
        self.active_button(self.chColorBt)

    def setup(self):
        self.old_x=None
        self.old_y=None
        self.line_width="2"
        self.color=self.DEFAULT_COLOR
        self.ereaser_on=False
        self.active_button=self.pen_poga
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)

    def active_button(self):
        pass

    def paint(self,event):
        paint_color='white' if self.ereaser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,event.x,event.y,
            width=self.line_width,fill=paint_color,
            capstyle=ROUND,smooth=True,splinesteps=36)
        self.old_x=event.x
        self.old_y=event.y

    def reset(self,event):
        self.old_x,self.old_y=None,None


if __name__=='__main__':
    zimet()
