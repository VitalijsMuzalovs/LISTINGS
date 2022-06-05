import tkinter as tk
from turtle import width

# Slider

class Otrs:
    def __init__(self,win):
        self.master=win
        
        # Frame
        self.frame=tk.Frame(self.master,width=300,height=300,bg='white')
        self.frame.pack(fill='both')
        

        # create slider/scale
        self.scale=tk.Scale(self.frame,label="Skala!",from_=0,to=10,orient="horizontal",
                            showvalue=True,tickinterval=1,resolution=1,command=self.print,
                            troughcolor='blue',bg='grey',width=20,length=150)
        self.scale.place(x=0,y=0)
        print(self.scale.winfo)

        # create button
        self.bt = tk.Button(self.frame,text='Disable',command=self.cmdDisable)
        self.bt.place(x=30,y=100)

    def print(self,value):
        print(value)
    
    def cmdDisable(self):
        self.scale.config(state='disabled',troughcolor='grey')

win=tk.Tk()
win.geometry("700x250")
win.title("Mans logs")


win2=Otrs(win)

win.mainloop()