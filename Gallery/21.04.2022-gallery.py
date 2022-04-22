from tkinter import *
from PIL import ImageTk, Image

win=Tk()

def fwClick(img_num):
    global vieta
    global back,forward
    # vieta=Label(image=imgList[img_num-1])
    vieta.grid_forget()
    vieta=Label(image=imgList[img_num+1])

    

    if img_num==5:
        forward=Button(win,text=">>",state=DISABLED)

    forward=Button(win,text=">>",command=lambda:fwClick(img_num+1))
    back=Button(win,text="<<",command=lambda:bkClick(img_num-1))

    vieta.grid(row=0,column=0,columnspan=3)
    back.grid(row=1,column=0)
    forward.grid(row=1,column=2)


def bkClick(img_num):
    global vieta
    global back,forward
    vieta.grid_forget()
    vieta=Label(image=imgList[img_num-1])
    forward=Button(win,text=">>",command=lambda:fwClick(img_num+1))
    back=Button(win,text="<<",command=lambda:bkClick(img_num-1))

    if img_num==1:
        forward=Button(win,text="<<",state=DISABLED)
    vieta.grid(row=0,column=0,columnspan=3)
    back.grid(row=1,column=0)
    forward.grid(row=1,column=2)


img1=ImageTk.PhotoImage(Image.open("Gallery\img\Logo1.jpg"))
img2=ImageTk.PhotoImage(Image.open("Gallery\img\Logo2.jpg"))
img3=ImageTk.PhotoImage(Image.open("Gallery\img\Logo3.jpg"))
img4=ImageTk.PhotoImage(Image.open("Gallery\img\Logo4.jpg"))
img5=ImageTk.PhotoImage(Image.open("Gallery\img\Logo5.jpg"))

imgList = [img1,img2,img3,img4,img5]
imgList[2]

vieta=Label(image=img1)
back=Button(win,text="<<",command=lambda:bkClick(1))
forward=Button(win,text=">>",command=lambda:fwClick(1))
beigt=Button(win,text="Close",command=win.quit)

vieta.grid(row=0,column=0,columnspan=3)
beigt.grid(row=1,column=1)

back.grid(row=1,column=0)
forward.grid(row=1,column=2)

win.mainloop()