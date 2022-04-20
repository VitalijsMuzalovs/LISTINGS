from tkinter import*

win=Tk()
win.title("TicTacToe")
# mansLogs.iconbitmap("")
btX = "35"
pdY="30"


for i in range(0,10):
    myExpr = "cell"+str(i)+"=Button(win,padx=btX,pady=pdY)"
    exec(myExpr)

m=0
for i in range(0,3):
    for j in range(0,3):
        myExpr2="cell"+str(m)+".grid(row="+str(i)+",column="+str(j)+")"
        exec(myExpr2)
        m+=1

win.mainloop()