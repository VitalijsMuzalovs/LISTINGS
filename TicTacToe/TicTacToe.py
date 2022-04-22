from importlib.machinery import WindowsRegistryFinder
from tkinter import*
from tkinter import messagebox

win=Tk()
win.title("TicTacToe")
# mansLogs.iconbitmap("")
pdX = "6"
pdY="3"

playerX=True
skait=0

def btClick(btName):
    global playerX,skait
    if btName["text"]=="" and playerX==True:
        btName["text"]="X"
        playerX=False
        skait+=1
        winCase()
    elif btName["text"]==""  and playerX==False:
        btName["text"]="O"
        playerX=True
        skait+=1
        winCase()
    else:
        messagebox.showerror("Error!","Something wrong!")
    return 0

def winCase():
    global winner
    winner=False
    if (cell0["text"]=="X" and cell1["text"]=="X" and cell2["text"]=="X" or
        cell3["text"]=="X" and cell4["text"]=="X" and cell5["text"]=="X" or
        cell6["text"]=="X" and cell7["text"]=="X" and cell8["text"]=="X" or

        cell0["text"]=="X" and cell3["text"]=="X" and cell6["text"]=="X" or
        cell1["text"]=="X" and cell4["text"]=="X" and cell7["text"]=="X" or
        cell2["text"]=="X" and cell5["text"]=="X" and cell8["text"]=="X" or

        cell0["text"]=="X" and cell4["text"]=="X" and cell8["text"]=="X" or
        cell2["text"]=="X" and cell4["text"]=="X" and cell6["text"]=="X"):

        winner=True
        messagebox.showinfo("WIN!","WINNER!")
    elif (cell0["text"]=="O" and cell1["text"]=="O" and cell2["text"]=="O" or 
        cell3["text"]=="O" and cell4["text"]=="O" and cell5["text"]=="O" or
        cell6["text"]=="O" and cell7["text"]=="O" and cell8["text"]=="O" or

        cell0["text"]=="O" and cell3["text"]=="O" and cell6["text"]=="O" or
        cell1["text"]=="O" and cell4["text"]=="O" and cell7["text"]=="O" or
        cell2["text"]=="O" and cell5["text"]=="O" and cell8["text"]=="O" or

        cell0["text"]=="O" and cell4["text"]=="O" and cell8["text"]=="O" or
        cell2["text"]=="O" and cell4["text"]=="O" and cell6["text"]=="O"):
        
        winner=True
        messagebox.showinfo("WIN!","WINNER!")
    elif skait==9 and winner==False:
        messagebox.showinfo("DRAW","It's a DRAW!\nGAME OVER!")
    return 0

for i in range(0,10):
    myExpr = "cell"+str(i)+"=Button(win,width=pdX,height=pdY,text='',font=('Helvetica',24),command=lambda:btClick(cell"+str(i)+"))"
    exec(myExpr)

m=0
for i in range(0,3):
    for j in range(0,3):
        myExpr2="cell"+str(m)+".grid(row="+str(i)+",column="+str(j)+")"
        exec(myExpr2)
        m+=1

win.mainloop()