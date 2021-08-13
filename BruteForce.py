import Problem
import itertools
from random import randrange

def get_surrounding(board, i, j):
  size = len(board)
  result = []
  for y in range(-1, 2):
    result += [board[i + x][j + y] for x in  range(-1, 2) if 0 <= i + x < size and 0 <= j + y < size]
  return sorted(result)

def get_all_surrounding(board, puzzle, size):
    surr_set = []
    for p in range(size):
        for k in range(size):
            if puzzle[p][k] != -1:
                surr = get_surrounding(board, p, k)
                surr_set.append(set(surr))
    return surr_set

def get_surrounding_intersect(surr_set):
    insct = surr_set[0]
    for surr in surr_set:
        insct = insct.intersection(surr)
    return insct

def brute_force(board, puzzle):
    print(board, puzzle)
    color_nums = [k for p in puzzle for k in p if k != -1]
    print(color_num)
    result = []
    for i in board:
        for k in i:
            result.append(k)
    size = len(color_num)
    surr_set = get_all_surrounding(board, puzzle, size)
    
    return result
def solve(p):
    result = brute_force(p.board, p.puzzle)
    pass