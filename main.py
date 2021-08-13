import backtrack as bt
from AStar import solve
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
        #'test_case/input3.txt',
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
        # solution = bf.solve(problem[1])


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
        if solution != None:
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
    p = Problem(read_file('test_case/input3.txt'))
    res = p.gen_all_CNF()
    pos=[x for x in res if sum(x)> 0]
    neg=[x for x in res if sum(x) < 0]
    print(f'Total: {len(res)}')
    #for it in res:
    #    print(it)
    size = p.size
    heuristic = -1
    exclude_list = [] # list chua phan tu xet roi
    while heuristic != 0:
        res_1 = []
        for i in range(size):
            for j in range(size):
                if p.board[i][j] not in exclude_list:
                    res_1.append((-p.board[i][j], (len([x for x in neg if -p.board[i][j] in x]))))# + len([x for x in pos if p.board[i][j] in x]))))
        res_1 = sorted(res_1, key = lambda x : x[1], reverse = True)

        h = res_1[0]
        heuristic = h[1]
        if heuristic > 0:
            exclude_list.append(h[0])
        print(f'Chosen: {h[0]} , heuristic: {heuristic}')
    
        if len(exclude_list) > 0:
            neg = [x for x in neg if exclude_list[-1] not in x]
            #pos = [x for x in pos if exclude_list[-1] not in x]
            #res = [x for x in pos if -exclude_list[-1] not in x]
            #print(res)

    print(exclude_list)
    
    solution = [-(x  + 1) if -(x  + 1) in exclude_list else (x + 1)  for x in range(size ** 2)]
    
    #print(sorted(exclude_list))
    print(f"Your solution   : {solution}")

    print(p.check_solution(solution))
    
    p.show(solution)
    #res_1.sort(key = lambda x : len(x[1]))
    #for k in res_1:
    #    print(f'Exclude {k[0]} : {len(k[1])}')
    
#main_test()
