from tkinter import *
from tkinter.colorchooser import askcolor
from unittest.mock import DEFAULT

class zimet(object):
    DEFAULT_PEN_SIZE=5.0    # ja nebūs defaltie, tad nevarēs arī mainīt
    DEFAULT_COLOR="black"
    
    def __init__(self):
        self.logs=Tk()

        #poga zīmulim
        self.pen_poga=Button(self.logs, text="zīmulis", command=self.lietot_zim)
        self.pen_poga.grid(row=0, column=0)
        # poga krāsu izvēlei
        self.krasu_poga=Button(self.logs, text="krāsa", command=self.izv_krasa)
        self.krasu_poga.grid(row=0, column=2)        
        #apgabalu zīmēšanai
        self.c=Canvas(self.logs, bg="white", width=500, height=500)
        self.c.grid(row=1, columnspan=5)
        self.setup()
        self.logs.mainloop()

    def lietot_zim(self):
        self.active_button(self.pen_poga)


    def izv_krasa(self):
        self.ereaser_on=False
        self.color=askcolor(color=self.color)[1]
        self.active_button(self.krasu_poga)# !!!!

# nosakam sākuma uzstādījumus, šo jāizsauc pirms mainloop, lai atjaunojas šie uzstādījumi:
    def setup(self):
        self.old_x=None
        self.old_y=None
        self.line_width="8"
        self.color=self.DEFAULT_COLOR
        self.ereaser_on=False
        self.active_button=self.pen_poga
        self.c.bind("<B1-Motion>", self.paint)
        self.c.bind("<ButtonRelease-1>", self.reset)

# pašās beigās var padarboties.
    def active_button(self):
        pass

    def paint(self, event):
        paint_color="white" if self.ereaser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, 
                                width=self.line_width, fill=paint_color,
                                capstyle=ROUND, smooth=TRUE, splinesteps=36)      #ja nebūs līnijas biezuma, tad neuzzimēs neko!
        self.old_x=event.x
        self.old_y=event.y

    def reset(self, event):
        self.old_x, self.old_y=None, None

if __name__=="__main__":
    zimet()


