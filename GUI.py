from tkinter import *
from tkinter import filedialog as fd 
from math import sqrt
from Problem import Problem
from tkinter.messagebox import showinfo
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

    def run_solution(self, i, j, size, heu):
        index = i*size + j
        self.heu.config(text=f'Step: {index + 1}, Heuristic: {heu}')
        self.square[index].config(bg='#ee161f',fg='#000000')
        self.square[index].after(int(self.delayTime * 1000))
        self.update()

    def start(self):
        for s in self.square:
            s.config(bg="#027403", fg='#ffffff')
        if self.square:
            p = Problem(self.matrix)
            res = p.gen_all_CNF()
            size = p.size
            heuristic = -1
            exclude_list = [] # list chua phan tu xet roi
            while heuristic != 0:
                res_1 = dict()
                for i in range(size):
                    for j in range(size):
                        if p.board[i][j] in exclude_list:
                            continue
                        elif -p.board[i][j] in exclude_list:
                            continue
                        else:
                            for x in res:
                                if p.board[i][j] in x:
                                    if -p.board[i][j] in res_1:
                                        res_1[-p.board[i][j]][1] += 1
                                    if p.board[i][j] in res_1:
                                        if res_1[p.board[i][j]][0] > len(x):
                                            res_1[p.board[i][j]][0] = len(x)
                                        res_1[p.board[i][j]][1] -= 1 # use the number of time it occur to a second heuristic
                                    else:
                                        res_1[p.board[i][j]] = [len(x), -1]
                                elif -p.board[i][j] in x:
                                    if p.board[i][j] in res_1:
                                        res_1[p.board[i][j]][1] += 1
                                    if -p.board[i][j] in res_1:
                                        if res_1[-p.board[i][j]][0] > len(x):
                                            res_1[-p.board[i][j]][0] = len(x)
                                        res_1[-p.board[i][j]][1] -= 1 # use the number of time it occur to a second heuristic
                                    else:
                                        res_1[-p.board[i][j]] = [len(x), -1]
                                else:
                                    if sum(x) > 0:
                                        if p.board[i][j] in res_1:
                                            res_1[p.board[i][j]][1] -= 1
                                    elif sum(x) < 0:
                                        if -p.board[i][j] in res_1:
                                            res_1[-p.board[i][j]][1] -= 1
                if len(res_1) == 0:
                    break
                key = min(res_1, key=res_1.get)
                heuristic = res_1[key][0]
                if heuristic > 0:
                    exclude_list.append(key)
                    res = [x for x in res if key not in x]
                    for y in res:
                        if -key in y:
                            y.remove(-key)
                if key > 0:
                    self.run_solution((abs(key)-1)//size, (abs(key)-1) % size, size, heuristic)
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
        lbl = Label(self, text=f'...{name[len(name) - 20:len(name)]}', height=2, width=20, bg='#f9f9f9')
        lbl.grid(column=0, row=2)
        lbl = Label(self, text="", height=2, width=20, bg='#eae9ea')
        lbl.grid(column=0, row=3)
        self.matrix = read_file(name)
        self.init_all_square('#ffffff', self.matrix)
        self.updateInput = Entry(self)
        self.updateInput.insert(END, self.delayTime)
        self.updateInput.grid(column=0, row=3)

    def popup_bonus(self):
        win = Toplevel()
        win.wm_title("A* Trace")

        l = Label(win, text="A* run completely", height=10, width=30)
        l.grid(row=0, column=0)

        b = Button(win, text="Done", command=win.destroy)
        b.grid(row=1, column=0)

if __name__ == '__main__':
    root = Tk()
    root.geometry("1200x800+300+300")
    app = Application(root)
    app.mainloop()


