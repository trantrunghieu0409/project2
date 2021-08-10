import Problem
import numpy as np
from itertools import combinations
class GenerateProblem:
    def __init__(self, size):
        """ Initialization of container.
        :param size: size of a puzzle
        :param from_file: loads classifier if puzzle is initialized from file
        """
        self.size = size
        self.puzzle = np.zeros((size[0], size[1]))
    def generate_random(self):
        """
        Generates random fill-a-pix puzzle.
        :return: solution of generated puzzle
        """
        self.puzzle += 100
        solution = np.zeros(self.size)
        for i, row in enumerate(self.puzzle):
            for j, el in enumerate(row):
                if np.random.random() < 0.5:
                    # number of black squares in neighbourhood
                    curr = len([[a, b] for a in range(max(0, i - 1), min(i + 2, self.size[0]))
                               for b in range(max(0, j - 1), min(j + 2, self.size[1]))
                               if solution[a, b] == 1])

                    # unfilled squares in neighbourhood (not including surely unfilled)
                    small = [[a, b] for a in range(max(0, i - 1), min(i + 2, self.size[0]))
                             for b in range(max(0, j - 1), min(j + 2, self.size[1]))
                             if solution[a, b] == 0]
                    if curr < len(small):
                        el = np.random.randint(curr, len(small) + 1)
                        self.puzzle[i, j] = el
                        while curr < el:
                            for (x, y) in small:
                                if solution[x, y] == 0:
                                    if np.random.random() < 0.9:
                                        solution[x, y] = 1
                                        curr += 1
                                        if el == curr:
                                            break
                        for (x, y) in small:
                            if solution[x, y] == 0:
                                solution[x, y] = -1

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if solution[i, j] == 0:
                    solution[i, j] = -1
        return solution
def get_surrounding(board, i, j):
  size = len(board)
  result = []
  for y in range(-1, 2):
    result += [board[i + x][j + y] for x in  range(-1, 2) if 0 <= i + x < size and 0 <= j + y < size]
  return sorted(result)
def count_surr(board, i, j):
    pass
def add_to_sol(solution, it):
    pass
def pop_out_sol(solution, it):
    pass
def Backtrack(puzzle, board, solution, i, j):
    if j == len(board):
        i+=1
        j = 0
    if i == len(board):
        return solution
    result = None
    if puzzle[i][j] != '.':
        for it in combinations(get_surrounding(board[i][j]), puzzle[i][j]):
            add_to_sol(solution, it)
            if count_surr(board, i, j) > puzzle[i][j]:
                return None
            result = Backtrack(puzzle, board, solution, i, j+1)
            if result != None:
                return result
            pop_out_sol(solution, it)
    return None



def solve(p):
    matrix = p.input()
    cnf = p.cnf()
    solution = p.matrix
    pass
