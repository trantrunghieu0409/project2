import Problem
from itertools import *
from random import randrange

def get_surrounding(board, i, j):
  size = len(board)
  result = []
  for y in range(-1, 2):
    result += [board[i + x][j + y] for x in  range(-1, 2) if 0 <= i + x < size and 0 <= j + y < size]
  return sorted(result)

def brute_force(board, puzzle, p):
    result = [-k for b in board for k in b]
    size = len(board)
    lst = []
    for i in range(size):
        for j in range(size):
            k = puzzle[i][j]
            if k != -1:
                surr = get_surrounding(board, i, j)
                c = list(combinations(surr, k))
                lst.append(c)
    rs = []
    for num in range(size * size + 1):
        cbn_lst = list(combinations(set([k for i in lst for k in i]), num))
        for cn in cbn_lst:
            result_check = result.copy()
            inter = set([j for i in cn for j in i])
            for i in inter:
                result_check[i - 1] = - result_check[i - 1]
            rs.append(result_check)
            if p.check_solution(result_check) == True:
                return result_check
    if [1, -2, 3, -4, -5, -6, -7, 8 ,9] in rs:
        print("success")
        # return [1, -2, 3, -4, -5, -6, -7, 8 ,9] 
    return []
    
def solve(p):
    result = brute_force(p.board, p.puzzle, p)
    return result
