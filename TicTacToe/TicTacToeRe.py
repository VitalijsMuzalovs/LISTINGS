from importlib.machinery import WindowsRegistryFinder
from msilib.schema import Class
from tkinter import*
from tkinter import messagebox


# mansLogs.iconbitmap("")


playerX=True
skait=0

class Field:
    def __init__(self):
        self.win=Tk()
        self.win.title("TicTacToe")
        self.pdX = "6"
        self.pdY="3"
        # for i in range(0,10):
        #     myExpr = "self.cell"+str(i)+"=Button(self.win,width=self.pdX,height=self.pdY,text='',font=('Helvetica',24),command=lambda:self.btClick(self.cell"+str(i)+"))"
        #     exec(myExpr)
        
        # print(str(self.cell0.__dir__))

        self.cell0=Button(self.win,width=self.pdX,height=self.pdY,text='',font=('Helvetica',24),command=lambda:self.btClick(self.cell0))
        self.cell1=Button(self.win,width=self.pdX,height=self.pdY,text='',font=('Helvetica',24),command=lambda:self.btClick(self.cell1))
        self.cell2=Button(self.win,width=self.pdX,height=self.pdY,text='',font=('Helvetica',24),command=lambda:self.btClick(self.cell2))
        self.cell3=Button(self.win,width=self.pdX,height=self.pdY,text='',font=('Helvetica',24),command=lambda:self.btClick(self.cell3))
        self.cell4=Button(self.win,width=self.pdX,height=self.pdY,text='',font=('Helvetica',24),command=lambda:self.btClick(self.cell4))
        self.cell5=Button(self.win,width=self.pdX,height=self.pdY,text='',font=('Helvetica',24),command=lambda:self.btClick(self.cell5))
        self.cell6=Button(self.win,width=self.pdX,height=self.pdY,text='',font=('Helvetica',24),command=lambda:self.btClick(self.cell6))
        self.cell7=Button(self.win,width=self.pdX,height=self.pdY,text='',font=('Helvetica',24),command=lambda:self.btClick(self.cell7))
        self.cell8=Button(self.win,width=self.pdX,height=self.pdY,text='',font=('Helvetica',24),command=lambda:self.btClick(self.cell8))
        # print(a)

        m=0
        for i in range(0,3):
            for j in range(0,3):
                myExpr2="self.cell"+str(m)+".grid(row="+str(i)+",column="+str(j)+")"
                exec(myExpr2)
                m+=1
        # self.cell0.grid(row=0,column=0)
        self.win.mainloop()

    def btClick(self,btName):
        global playerX,skait
        if btName["text"]=="" and playerX==True:
            btName["text"]="X"
            playerX=False
            skait+=1
            self.winCase()
        elif btName["text"]==""  and playerX==False:
            btName["text"]="O"
            playerX=True
            skait+=1
            self.winCase()
        else:
            messagebox.showerror("Error!","Something wrong!")

    def winCase(self):
        global winner
        winner=False
        if (self.cell0["text"]=="X" and self.cell1["text"]=="X" and self.cell2["text"]=="X" or
            self.cell3["text"]=="X" and self.cell4["text"]=="X" and self.cell5["text"]=="X" or
            self.cell6["text"]=="X" and self.cell7["text"]=="X" and self.cell8["text"]=="X" or

            self.cell0["text"]=="X" and self.cell3["text"]=="X" and self.cell6["text"]=="X" or
            self.cell1["text"]=="X" and self.cell4["text"]=="X" and self.cell7["text"]=="X" or
            self.cell2["text"]=="X" and self.cell5["text"]=="X" and self.cell8["text"]=="X" or

            self.cell0["text"]=="X" and self.cell4["text"]=="X" and self.cell8["text"]=="X" or
            self.cell2["text"]=="X" and self.cell4["text"]=="X" and self.cell6["text"]=="X"):

            winner=True
            messagebox.showinfo("WIN!","WINNER!")
        elif (self.cell0["text"]=="O" and self.cell1["text"]=="O" and self.cell2["text"]=="O" or 
            self.cell3["text"]=="O" and self.cell4["text"]=="O" and self.cell5["text"]=="O" or
            self.cell6["text"]=="O" and self.cell7["text"]=="O" and self.cell8["text"]=="O" or

            self.cell0["text"]=="O" and self.cell3["text"]=="O" and self.cell6["text"]=="O" or
            self.cell1["text"]=="O" and self.cell4["text"]=="O" and self.cell7["text"]=="O" or
            self.cell2["text"]=="O" and self.cell5["text"]=="O" and self.cell8["text"]=="O" or

            self.cell0["text"]=="O" and self.cell4["text"]=="O" and self.cell8["text"]=="O" or
            self.cell2["text"]=="O" and self.cell4["text"]=="O" and self.cell6["text"]=="O"):
            
            winner=True
            messagebox.showinfo("WIN!","WINNER!")
        elif skait==9 and winner==False:
            messagebox.showinfo("DRAW","It's a DRAW!\nGAME OVER!")
        return 0
Field()