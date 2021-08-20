import backtrack as bt
import AStar as astar
import pysat_CNF as py
import BruteForce as bf
import time
from Problem import Problem
import sys

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

def main(input_file, output_file, algorithm = 'pysat'):
    

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
        print(f"Running {algorithm}:... ")
        
        start = time.time()

        # Your algorithm
        # Should have a line: solution = ....
        if algorithm == 'pysat':
            solution = py.solve(problem)
        elif algorithm == 'astar':
            solution = astar.solve(problem)
        elif algorithm == 'backtrack':
            solution = bt.solve(problem)
        else:
            solution = bf.solve(problem)
        # end clock
        end = time.time()    
        
        # print the interval + solution
        result.append((solution, end - start))
    print('You can see solution in output.txt')
    original_stdout = sys.stdout
    with open(output_file, 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
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
        sys.stdout = original_stdout # Reset the standard output to its original value
        f.close()

#----------------------------------------------------------------------
#Run this if you want to show result to file
if __name__ == '__main__':
    
    input_file = [
        # file you want to test
        # remember to put ',' at the end 

        'test_case/input.txt',
        'test_case/input2.txt',
        'test_case/input3.txt',
        'test_case/input4.txt',
        'test_case/input5.txt',
    ]
    
    output_file = "output.txt" # file show result

    algo = {
        0: 'pysat',
        1: 'astar',
        2: 'backtrack',
        3: 'bruteforce',
    }
    chosen_algo = algo[0] # change number inside brackets if you want to change algorithm

    main(input_file, output_file, chosen_algo)

