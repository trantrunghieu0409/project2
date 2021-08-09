import numpy as np
from itertools import combinations

class Problem:
    puzzle = list(list())

    """
    board -> position matrix:
    Ex:
    1 2 3 4 5
    6 7 8 9 10
    ...
    """
    board = list(list()) 

    size = int()

    def __init__(self, matrix):
        self.puzzle = [x[:] for x in matrix]
        self.size = len(self.puzzle)
        self.board = np.reshape(range(1, self.size*self.size+1, 1), (self.size, self.size))

    def get_size(self):
        """
        get size of puzzle (size x size)
        """
        return self.size

    def copy(self):
        """
        return a copy of puzzle
        """
        return [x[:] for x in self.puzzle]
    
    def check_solution(self, solution):
        return True

    def show(self, solution):
        """
        True -> Green
        False -> Red
        solution can be in 2 forms:
        1. list() , ex: [-1, 2, 3, -4, 5 ...]
        -1 means False -> color at position 1 is Red

        2. list(list())
        ex: [[1,2,3], [-4,-5,6],...]

        Visualize solution
        """
        if type(solution) is list:
            # Form 1
            if type(solution[0]) is int:
                for i in range(self.size):
                    for j in range(self.size):
                        if i*self.size+j+1 in solution:
                            print('G', end=' ')
                        else:
                            print('_', end=' ')
                    print('')

            # Form 2
            elif type(solution[0]) is list:
                for i in range(self.size):
                    for j in range(self.size):
                        if solution[i][j] > 0:
                            print('G', end=' ')
                        else:
                            print('_', end=' ')
        
        print("Invalid solution!")
        pass
        
    def get_clauses(self, i, j):
        k = self.puzzle[i][j]
        clauses = []
        
        surr = get_surrounding(self.board, i, j)
        c = list(combinations(surr, k))

        for it in c:
            clause = list(it) + [x for x in surr if x not in list(it)]
            clauses += gen_clauses(k, np.array(clause))
        return clauses

    def gen_one_CNF(self, i , j):
        return self.get_clauses(i , j)

    def gen_all_CNF(self):
        clauses = []
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] != -1:
                    clauses += self.gen_one_CNF(i,j)
        return clauses

def get_surrounding(matrix, i, j):
    size = len(matrix)
    result = []
    for y in range(-1, 2):
        result += [matrix[i + x][j + y] for x in  range(-1, 2) if 0 <= i + x < size and 0 <= j + y < size]
    return sorted(result)

def gen_clauses(k, list_cells):
    # p <-> q :
    # (1 ^ 2) <-> -3^-5^-6^-7
    # (-1 v -2 v -3) ^ ... ^ (3 v 5 v 6 v 7 v 1) ^ (3 v 5 v 6 v 7 v 2)
    
    clauses = []
    left = list_cells[:k] 
    right = list_cells[k:]

    for it in right:
      clauses.append(np.append(-left, -it))

    for it in left:
      clauses.append(np.append(right, it))

    return clauses


