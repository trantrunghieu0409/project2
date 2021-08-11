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
def count_surr(board, i, j, solution):
    surr = get_surrounding(board, i, j)
    count = 0
    for k in surr:
        if k in solution:
            count += 1
    return count

def check_surr(board, i, j, solution, puzzle):
    size = len(board)
    for k in range(-1, 1):
        for t in range(-1, 2):
            if k == 0 and t == 1:
                continue
            #if surround is another element, check it
            if 0 <= i + k < size and 0 <= j + t < size and puzzle[i + k][j + t] != -1:
                if count_surr(board, i+k, j+t, solution) != puzzle[i+k][j+t]:
                    return False
            #if surround added_item is another element but not the current item
            elif 0 <= i + k < size and 0 <= j + t < size and (t!=0 or k!=0) and board[i+k][j+t] in solution:
                #print(count_surr(board, i + k, j + t, solution), puzzle[i+k][j+t], i + k, j + t)
                #check that item
                if not check_surr(board,i+k, j+t, solution, puzzle):
                    return False
    return True

def Backtrack(puzzle, board, solution, i, j):
    if j == len(board):
        i += 1
        j = 0
    if i == len(board):
        return solution
    result = None
    if puzzle[i][j] != -1:
        s = solution.copy()
        for it in combinations(get_surrounding(board, i, j), puzzle[i][j]):
            for k in it:
                if k not in solution:
                    solution.append(k)
            if check_surr(board, i, j, solution, puzzle):
                result = Backtrack(puzzle, board, solution, i, j+1)
                if result != None:
                    return result
            solution = s.copy()
        return None
    else:
        if check_surr(board, i, j, solution, puzzle):
            return Backtrack(puzzle, board, solution, i, j+1)
    return None



def solve(p):
    solution = []
    rs = Backtrack(p.puzzle, p.board, solution, 0,0)
    # format solution
    rs = [x + 1 if x + 1 in rs else -(x + 1) for x in range(p.size ** 2)]
    return rs
