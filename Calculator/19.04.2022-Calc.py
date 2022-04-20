from tkinter import*

mansLogs=Tk()
mansLogs.title("Calculator")
# mansLogs.iconbitmap("")
btX = "40"
pdY="20"

def btClick(number):
    try:
        current=e.get()
        e.delete(0,END)
        newVal = str(current)+str(number)
        e.insert(0,newVal)
    except:
        return 0
    return 0

def pressClear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

def calculate(sign):
    global mathOp
    global num1
    mathOp = sign
    num1 = int(e.get())
    e.delete(0,END)
    return 0
    
def pressEqual():
    num2 = int(e.get())
    if mathOp=="+":
        rez = num1+num2
    elif mathOp=="-":
        rez = num1-num2
    elif mathOp=="/":
        rez = num1/num2
    elif mathOp=="*":
        rez = num1*num2
    else:
        rez=0
    e.delete(0,END)
    e.insert(0,str(rez))
    return 0


# Make it with FOR

e = Entry(mansLogs,width=15,font=("Arial Black",22) )

bt0=Button(mansLogs,text="0",padx=btX,pady=pdY,command=lambda:btClick(0))
bt1=Button(mansLogs,text="1",padx=btX,pady=pdY,command=lambda:btClick(1))
bt2=Button(mansLogs,text="2",padx=btX,pady=pdY,command=lambda:btClick(2))
bt3=Button(mansLogs,text="3",padx=btX,pady=pdY,command=lambda:btClick(3))
bt4=Button(mansLogs,text="4",padx=btX,pady=pdY,command=lambda:btClick(4))
bt5=Button(mansLogs,text="5",padx=btX,pady=pdY,command=lambda:btClick(5))
bt6=Button(mansLogs,text="6",padx=btX,pady=pdY,command=lambda:btClick(6))
bt7=Button(mansLogs,text="7",padx=btX,pady=pdY,command=lambda:btClick(7))
bt8=Button(mansLogs,text="8",padx=btX,pady=pdY,command=lambda:btClick(8))
bt9=Button(mansLogs,text="9",padx=btX,pady=pdY,command=lambda:btClick(9))
btEq=Button(mansLogs,text="=",padx=btX,pady=pdY,command=lambda:pressEqual())
btClear=Button(mansLogs,text="C",padx=btX,pady=pdY,command=lambda:pressClear())

myPlus=Button(mansLogs,text="+",padx=btX,pady=pdY,command=lambda:calculate("+"))
myMinus=Button(mansLogs,text="-",padx=btX,pady=pdY,command=lambda:calculate("-"))
myMult=Button(mansLogs,text="*",padx=btX,pady=pdY,command=lambda:calculate("*"))
myDevide=Button(mansLogs,text="/",padx=btX,pady=pdY,command=lambda:calculate("/"))

e.grid(row=1,column=1,columnspan=5)
bt7.grid(row=2,column=1)
bt8.grid(row=2,column=2)
bt9.grid(row=2,column=3)
bt4.grid(row=3,column=1)
bt5.grid(row=3,column=2)
bt6.grid(row=3,column=3)
bt1.grid(row=4,column=1)
bt2.grid(row=4,column=2)
bt3.grid(row=4,column=3)
bt0.grid(row=5,column=2)

myMinus.grid(row=2,column=4)
myPlus.grid(row=3,column=4)
myMult.grid(row=4,column=4)
myDevide.grid(row=5,column=4)


btEq.grid(row=5,column=3)
btClear.grid(row=5,column=1)


# TASK - add "*" and "/"
mansLogs.mainloop()