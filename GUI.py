from tkinter import *
from tkinter import filedialog as fd 

class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()
        self.choose_file()

    def initUI(self):
        self.parent.title("A* Trace")
        self.pack(fill=BOTH, expand=1)
    
    def choose_file(self):
        lbl = Label(self, text="Choose input file", height=2, width=20, bg='#ffffff')
        lbl.grid(column=0, row=2)

        btn = Button(self, text='Click to Open File', command=self.callback, bg='#377dff', highlightcolor='#0069d9', fg='#ffffff', bd='1px', height='2')
        btn.grid(column=1, row=2)

    def callback(self):
        name= fd.askopenfilename() 
        print(name)

root = Tk()
root.geometry("800x600+300+300")
app = Application(root)
root.mainloop()
