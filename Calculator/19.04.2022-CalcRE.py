from tkinter import*

mansLogs=Tk()
mansLogs.title("Calculator")
# mansLogs.iconbitmap("")
btX = "40"
pdY="20"

def btClick(number):
        current=e.get()
        e.delete(0,END)
        newVal = str(current)+str(number)
        e.insert(0,newVal)

def pressClear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

def calculate(sign):
    global mathOp
    global num1
    try:
        mathOp = sign
        num1 = int(e.get())
        e.delete(0,END)
    except ValueError:
        e.insert(0,'Not number!')
    return 0
    
def pressEqual():
    try:
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
    except:
        e.delete(0,END)
        e.insert('ERROR!')
    return 0

e = Entry(mansLogs,width=15,font=("Arial Black",22) )

for i in range(10):
    myExpr = "bt"+str(i)+"=Button(mansLogs,text="+str(i)+",padx=btX,pady=pdY,command=lambda:btClick("+str(i)+"))"
    exec(myExpr)

btEq=Button(mansLogs,text="=",padx=btX,pady=pdY,command=lambda:pressEqual())
btClear=Button(mansLogs,text="C",padx=btX,pady=pdY,command=lambda:pressClear())

myDict={"myPlus":'+',"myMinus":"-","myMult":"*","myDevide":"/"}

for myKey,v in myDict.items():
    myExpr = myKey+"=Button(mansLogs,text='"+v+"',padx=btX,pady=pdY,command=lambda:calculate('"+v+"'))"
    exec(myExpr)

e.grid(row=1,column=1,columnspan=5)

m=0
for i in range(5,1,-1):
    for j in range(1,4):
        if not(i==5 and j!=2):
            myExpr2="bt"+str(m)+".grid(row="+str(i)+",column="+str(j)+")"
            exec(myExpr2)
            m+=1

myMinus.grid(row=2,column=4)
myPlus.grid(row=3,column=4)
myMult.grid(row=4,column=4)
myDevide.grid(row=5,column=4)

btEq.grid(row=5,column=3)
btClear.grid(row=5,column=1)

mansLogs.mainloop()