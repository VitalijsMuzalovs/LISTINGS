import tkinter as tk

# Slider

def cmShow(a):
    e.config(text='Value: '+ a)
    return 0

win=tk.Tk()
win.geometry("300x100")
win.title("Mans logs")

e = tk.Label(win,width=22,bg="white",fg="black",font=("Arial Black",10),borderwidth=1,text="empty")
e.pack(anchor="n")

skala=tk.Scale(win,label="Pamēģini!",from_=0,to=10,orient="horizontal",showvalue=True,tickinterval=2,resolution=0.01,command=cmShow)
skala.pack()

win.mainloop()