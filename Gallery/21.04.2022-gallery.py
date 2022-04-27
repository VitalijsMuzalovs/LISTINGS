from tkinter import *
from PIL import ImageTk, Image

win=Tk()

img1=ImageTk.PhotoImage(Image.open("Gallery\img\Logo1.jpg"))
img2=ImageTk.PhotoImage(Image.open("Gallery\img\Logo2.jpg"))
img3=ImageTk.PhotoImage(Image.open("Gallery\img\Logo3.jpg"))
img4=ImageTk.PhotoImage(Image.open("Gallery\img\Logo4.jpg"))
img5=ImageTk.PhotoImage(Image.open("Gallery\img\Logo5.jpg"))

imgList = [img1,img2,img3,img4,img5]
imgList[1]

vieta=Label(image=img1)
vieta.grid(row=0,column=0,columnspan=3)

back=Button(win,text="<<",state=DISABLED,command=lambda:bkClick())
forward=Button(win,text=">>",command=lambda:fwClick(2))
beigt=Button(win,text="Close",command=win.quit)

beigt.grid(row=1,column=1)
back.grid(row=1,column=0)
forward.grid(row=1,column=2)

def fwClick(img_num):
    global vieta
    global back,forward

    forward=Button(win,text=">>",command=lambda:fwClick(img_num+1))
    if img_num==len(imgList):forward=Button(win,text=">>",state=DISABLED)
    back=Button(win,text="<<",command=lambda:bkClick(img_num-1))
    vieta.grid_forget()
    vieta=Label(image=imgList[img_num-1])

    vieta.grid(row=0,column=0,columnspan=3)
    back.grid(row=1,column=0)
    forward.grid(row=1,column=2)
    
def bkClick(img_num):
    global vieta
    global back,forward  

    forward=Button(win,text=">>",command=lambda:fwClick(img_num+1))
    back=Button(win,text="<<",command=lambda:bkClick(img_num-1))
    if img_num==1:back=Button(win,text="<<",state=DISABLED)
    vieta.grid_forget()
    vieta=Label(image=imgList[img_num-1])
    
    vieta.grid(row=0,column=0,columnspan=3)
    back.grid(row=1,column=0)
    forward.grid(row=1,column=2)

win.mainloop()