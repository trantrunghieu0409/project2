import Problem
import numpy as np
from itertools import combinations
import time

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

def Backtrack(puzzle, board, solution, i, j, app, size):
    if app is not None:
        app.reset_background()
        for k in solution:
            app.update_square2((abs(k)-1)//size, (abs(k)-1) % size, size, 0, app.countStep, app.green)
        app.after(1)
        app.update()
        app.countStep += 1
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
                result = Backtrack(puzzle, board, solution, i, j+1, app, size)    
                if result != None:
                    return result
            solution = s.copy()
        return None
    else:
        if check_surr(board, i, j, solution, puzzle):
            return Backtrack(puzzle, board, solution, i, j+1, app, size)
    return None



def solve(p, app=None):
    solution = []
    rs = Backtrack(p.puzzle, p.board, solution, 0,0, app, p.size)
    # format solution
    if rs != None:
        rs = [x + 1 if x + 1 in rs else -(x + 1) for x in range(p.size ** 2)]
    return rs

