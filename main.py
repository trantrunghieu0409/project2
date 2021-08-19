import backtrack as bt
import AStar as astar
import pysat_CNF as py
import BruteForce as bf
from Problem import Problem
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

def write_file(output_file, solution):
    pass

def main():
    
    input_file = [
        # file you want to test
        # remember to put ',' at the end ;) 
        #'test_case/input.txt',
        'test_case/input2.txt',
        # 'test_case/input3.txt',
        # 'test_case/input4.txt',
        #'test_case/input5.txt',
    ]

    problem_list = []
    for inp in input_file:
        matrix = read_file(inp)
        # formualte problem
        problem_list.append(Problem(matrix))

    # initialize
    duration = time.time() - time.time()
    # start clock

    # number of time to run
    result = []
    for problem in problem_list:
        print(f"Running:... ")
        
        start = time.time()

        # Your algorithm
        # Should have a line: solution = ....

        solution = py.solve(problem)
        #solution = bf.solve(problem)
        #solution = bt.solve(problem)
        #solution = astar.solve(problem)
        # end clock
        end = time.time()    
        
        # print the interval + solution
        result.append((solution, end - start))


    n_test = len(input_file)
    count = 0
    for i in range(n_test):
        print(".................................................................")
        p = problem_list[i]

        solution = result[i][0]
        time_run = result[i][1]
        
        print(f'Test case {i + 1}:' )
        print(f'Solution: {solution}')
        if solution != None and len(solution) > 0:
            print('Visualize:')
            p.show(solution)
            if p.check_solution(solution):
                print('=> Correct solution!')
                count+=1
            else:
                print('=> Wrong solution!')

        print(f'Time running: {time_run} (s)')
        
    print(".................................................................")
    print(f'Number of test cases: {n_test}')
    print(f'Number of success solution: {count}/{n_test}')
    print(f'Average time require: {sum([time for solution , time in result]) / n_test}')

#----------------------------------------------------------------------
#Run this if you want to show result
if __name__ == '__main__':
    main()



# This function is for debugging
def main_test():
    p = Problem(read_file('test_case/input4.txt'))
    res = p.gen_all_CNF()
    pos=[x for x in res if sum(x)> 0]
    neg=[x for x in res if sum(x) < 0]
    print(f'Total: {len(res)}')
    #print(res)
    #for it in res:
    #    print(it)
    size = p.size
    heuristic = -1
    exclude_list = [] # list chua phan tu xet roi
    while heuristic != 0:
        res_1 = dict()
        for i in range(size):
            for j in range(size):
                if p.board[i][j] not in exclude_list:
                    for x in res:
                        if p.board[i][j] in x:
                            # if min([len(y) for y in res if -p.board[i][j] in y]) == 1:
                            #     res_1[-p.board[i][j]] = 999
                            if p.board[i][j] in res_1:
                                if res_1[p.board[i][j]][0] > len(x):
                                    res_1[p.board[i][j]][0] = len(x)
                                    res_1[p.board[i][j]][1] += 1
                            else:
                                res_1[p.board[i][j]] = [len(x), 1]
                        elif -p.board[i][j] in x:
                            if -p.board[i][j] in res_1:
                                if res_1[-p.board[i][j]][0] > len(x):
                                    res_1[-p.board[i][j]][0] = len(x)
                                    res_1[-p.board[i][j]][1] += 1
                            else:
                                res_1[-p.board[i][j]] = [len(x), 1]

        if len(res_1) == 0:
            break
        key = min(res_1, key=res_1.get)
        # if -key in res_1:
        #     if res_1[key] == res_1[-key]:
        #         key = -key
        heuristic = res_1[key][0]
        if heuristic > 0:
            exclude_list.append(key)
            res = [x for x in res if key not in x]
            for y in res:
                if -key in y:
                    y.remove(-key)
        print(f'Chosen: {key} , heuristic: {heuristic}')
 
    heuristic = -1
    
    solution = sorted([x if x in exclude_list else -x for x in range(1, size**2+1)], key = lambda item: abs(item))#+ list({x[0] for x in neg if len(x) == 1})

    #print(sorted(exclude_list))
    print(f"Your solution   : {solution}")

    print(p.check_solution(solution))
    
    p.show(solution)
    #res_1.sort(key = lambda x : len(x[1]))
    #for k in res_1:
    #    print(f'Exclude {k[0]} : {len(k[1])}')
    
#main_test()
