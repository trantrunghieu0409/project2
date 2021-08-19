import Problem
from itertools import combinations

def brute_force(p):
    init_list = [x + 1 for x in range(p.size**2)]
    for k in range(p.size**2):
        c = combinations(init_list, k + 1)
        for it in c:
            result = init_list.copy()
            for index in it:
                result[index - 1] *= -1

            if p.check_solution(result):    
                return result
    return None

def solve(p):
    result = brute_force(p)
    return result
