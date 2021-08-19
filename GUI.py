from tkinter import *
from tkinter import filedialog as fd 
from math import sqrt
from Problem import Problem
import pysat_CNF as py
import time

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
        self.solution = None

    def initUI(self):
        self.parent.title("A* Trace")
        self.pack(fill=BOTH, expand=1)
        self.delayTime = 0.5
    
    def updateDelay(self):
        self.delayTime = float(self.updateInput.get())

    def control(self):
        lbl = Label(self, text="Choose input file", height=2, width=20, bg='#f9f9f9')
        lbl.grid(column=0, row=2)
        btnBrowser = Button(self, text='Browser', command=self.choose_file, bg='#377dff', highlightcolor='#0069d9', fg='#ffffff', bd='1px', height='2')
        btnBrowser.grid(column=1, row=2)
        btnStart = Button(self, text='Start', command=self.start, padx=10, bg='#377dff', highlightcolor='#0069d9', fg='#ffffff', bd='1px', height='2')
        btnStart.grid(column=3, row=2)
        self.updateInput = Entry(self)
        self.updateInput.insert(END, self.delayTime)
        self.updateInput.grid(column=0, row=3)
        self.btnUpdate = Button(self, text='Update', command=self.updateDelay, padx=10, bg='#377dff', highlightcolor='#0069d9', fg='#ffffff', bd='1px', height='2')
        self.btnUpdate.grid(column=1 , row=3)
        self.heu = Label(self, text="Step: 0, Heuristic: -1", height=2, width=20, bg='#f9f9f9')
        self.heu.grid(column=0, row=4)

    def run_solution(self, i, j, size):
        index = i*size + j
        self.heu.config(text=f'Step: {index + 1}, Heuristic: {i}')
        self.square[index].config(bg='#ee161f',fg='#000000')
        self.square[index].after(int(self.delayTime * 1000))
        self.update()

    def start(self):
        for s in self.square:
            s.config(bg="#027403", fg='#ffffff')
        if self.square:
            size = int(sqrt(len(self.solution)))
            for i in range(size):
                for j in range(size):
                    if self.solution[i* size + j] < 0:
                        self.run_solution(i, j, size)

    def init_square(self, txt, i, j, color):
        lbl = Label(self, text=txt, height=2, width=5, bg=color, bd='10px', borderwidth="2", relief="solid", fg='#000000')
        lbl.grid(column=j, row = i)
        return lbl

    def init_all_square(self, color, matrix):
        size = len(matrix)
        for i in range(size):
            for j in range(size):
                text = matrix[i][j] if matrix[i][j] != -1 else ""
                self.square.append(self.init_square(text, i + 3, j + 7, color))

    def choose_file(self):
        if self.square:
            for label in self.square:
                label.after(1000, label.destroy)
            self.square.clear()
        name= fd.askopenfilename()
        lbl = Label(self, text=f'...{name[len(name) - 20:len(name)]}', height=2, width=20, bg='#f9f9f9')
        lbl.grid(column=0, row=2)
        lbl = Label(self, text="", height=2, width=20, bg='#eae9ea')
        lbl.grid(column=0, row=3)
        self.matrix = read_file(name)
        problem = Problem(self.matrix)
        self.solution = py.solve(problem)
        self.init_all_square('#ffffff', self.matrix)
        self.updateInput = Entry(self)
        self.updateInput.insert(END, self.delayTime)
        self.updateInput.grid(column=0, row=3)

if __name__ == '__main__':
    root = Tk()
    root.geometry("1200x800+300+300")
    app = Application(root)
    app.mainloop()

