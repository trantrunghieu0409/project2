import time
from tkinter import *
import AStar as astar
from math import sqrt
import backtrack as bt
import pysat_CNF as py
import BruteForce as bf
from Problem import Problem
from tkinter import filedialog as fd 
from tkinter.messagebox import showinfo

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
        self.clicked = None
        self.grid(padx=20, pady=20)
        self.matrix = None
        self.square = []
        self.solution = None
        self.type = None
        self.countStep = None
        self.initUI()
        self.control()
        self.choose_algorithm()

    def initUI(self):
        self.parent.title("Visualization")
        self.pack(fill=BOTH, expand=1)
        self.delayTime = 0.5
        self.countStep = 1
        self.red = '#ee161f'
        self.green = '#027403'
    
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

    def update_square(self, i, j, size, heu, step, color):
        index = i*size + j
        self.heu.config(text=f'Step: {step}, Heuristic: {heu}')
        self.square[index].config(bg= color,fg='#000000')
        self.square[index].after(int(self.delayTime * 1000))
        self.update()

    def update_square2(self, i, j, size, heu, step, color):
        index = i*size + j
        self.heu.config(text=f'Step: {step}, Heuristic: {heu}')
        self.square[index].config(bg= color,fg='#000000')

    def run_solution(self, solution, color):
        size = int(sqrt(len(solution)))
        for i in range(size):
            for j in range(size):
                if solution[i*size + j] < 0:
                    self.update_square(i, j, size, 0, 0, color)

    def reset_background(self):
        for s in self.square:
            s.config(bg=self.red, fg='#ffffff')
        s.after(1000)
        
    def start(self):
        if self.type == 0 or self.type == 1:
            bg = self.green
        else:
            bg = self.red
        for s in self.square:
            s.config(bg=bg, fg='#ffffff')
        s.after(1000)
        self.update()
        matrix = Problem(self.matrix)
        if self.type is not None:
            if self.type == 0:
                solution = py.solve(matrix)
                self.run_solution(solution, self.red)
            elif self.type == 1:
                solution = astar.solve(matrix, self)
            elif self.type == 2:
                solution = bt.solve(matrix, self)
        self.popup_bonus()

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
        lbl1 = Label(self, text=f'...{name[len(name) - 20:len(name)]}', height=2, width=20, bg='#f9f9f9')
        lbl1.grid(column=0, row=2)
        lbl2 = Label(self, text="", height=2, width=20, bg='#eae9ea')
        lbl2.grid(column=0, row=3)
        self.matrix = read_file(name)
        self.init_all_square('#ffffff', self.matrix)
        self.updateInput = Entry(self)
        self.updateInput.insert(END, self.delayTime)
        self.updateInput.grid(column=0, row=3)

    def popup_bonus(self):
        win = Toplevel()
        win.wm_title("Visualization")

        l = Label(win, text="Run completely", height=10, width=30)
        l.grid(row=0, column=0)

        b = Button(win, text="Done", command=win.destroy)
        b.grid(row=1, column=0)

    def switch_type(self):
        opt = self.clicked.get()
        switcher = {
            "PySAT": 0,
            "A*": 1,
            "Backtrack": 2,
        }   
        self.type = switcher.get(opt, None)
        
    def choose_algorithm(self):
        self.clicked = StringVar()
        self.clicked.set('PySAT')   
        drop = OptionMenu(self, self.clicked, "PySAT","A*", "Backtrack")
        drop.grid(column=0, row=1)
        btn = Button(self, text='Choose Algorithm', command=self.switch_type)
        btn.grid(column=1, row=1)

if __name__ == '__main__':
    root = Tk()
    root.geometry("1200x800+300+300")
    app = Application(root)
    app.mainloop()

