from tkinter import Frame, Tk

class MyApp():
    def __init__(self):
        self.root = Tk()

        self.my_frame_red = Frame(self.root, bg='red',width=150)
        self.my_frame_red.grid(row=0, column=0, sticky='nsew')

        self.my_frame_blue = Frame(self.root, bg='blue',width=250)
        self.my_frame_blue.grid(row=0, column=1, sticky='nsew')

        self.root.grid_rowconfigure(0, minsize=20, weight=1)
        self.root.grid_columnconfigure(0, minsize=20, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.root.mainloop()

if __name__ == '__main__':
    app = MyApp()
