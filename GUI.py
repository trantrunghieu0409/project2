from tkinter import *
from tkinter import filedialog as fd 

def read_file(input_file):
    """
    Read input from file

    Returns a matrix

    Note: character '.' will be convert into -1.
    """
    matrix = list()
    with open(input_file, 'r') as f:
        for line in f:
            matrix.append([int(x) if x != '.' else -1 for x in line.split()])    
        f.close()
    return matrix

class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="#eae9ea")
        self.parent = parent
        self.initUI()
        self.control()
        self.grid(padx=20, pady=20)
        self.matrix = None
        self.square = []

    def initUI(self):
        self.parent.title("A* Trace")
        self.pack(fill=BOTH, expand=1)
    
    def control(self):
        lbl = Label(self, text="Choose input file", height=2, width=20, bg='#f9f9f9')
        lbl.grid(column=0, row=2)
        btn = Button(self, text='Browser', command=self.choose_file, bg='#377dff', highlightcolor='#0069d9', fg='#ffffff', bd='1px', height='2')
        btn.grid(column=1, row=2)
        btn = Button(self, text='Start', command=self.start, padx=10, bg='#377dff', highlightcolor='#0069d9', fg='#ffffff', bd='1px', height='2')
        btn.grid(column=3, row=2)
    
    def start(self):
        for s in self.square:
            s.config(bg="#027403")

    def init_square(self, txt, i, j, color):
        lbl = Label(self, text=txt, height=5, width=10, bg=color, bd='10px', borderwidth="2", relief="solid")
        lbl.grid(column=j, row = i)
        return lbl

    def init_all_square(self, color, matrix):
        size = len(matrix)
        for i in range(size):
            for j in range(size):
                text = matrix[i][j] if matrix[i][j] != -1 else ""
                self.square.append(self.init_square(text, i + 4, j + 4, color))

    def choose_file(self):
        if self.square:
            for label in self.square:
                label.after(1000, label.destroy)
            self.square.clear()
        name= fd.askopenfilename()
        lbl = Label(self, text=name, height=2, width=20, bg='#f9f9f9')
        lbl.grid(column=0, row=2)
        lbl = Label(self, text="", height=2, width=20, bg='#eae9ea')
        lbl.grid(column=0, row=3)
        self.matrix = read_file(name)
        self.init_all_square('#ffffff', self.matrix)

root = Tk()
root.geometry("1200x800+300+300")
app = Application(root)
app.mainloop()
