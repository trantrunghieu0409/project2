from backtrack import solve
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
    # initialize
    matrix = read_file('input.txt')

    # formualte problem
    p = Problem(matrix)
         
    # Your algorithm
    solution = py.solve(p)

    # Write into output file
    write_file('output.txt', solution)    


def main_test():
    
    input_file = [
        # file you want to test
        # remember to put ',' at the end ;) 
        'input.txt', 
        'input2.txt',
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


        # end clock
        end = time.time()    
        
        # print the interval + solution
        result.append((solution[:].copy(), end - start))

    print(".................................................................")
    n_test = len(input_file)
    count = 0
    for i in range(n_test):
        p = problem_list[i]
        solution = result[i][0]
        time_run = result[i][1]

        print(f'Test case {i + 1}:' )
        print(f'Solution: {solution}')
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
# call main function
#if __name__ == '__main__':
#    main()

# Call main_test() if you want to show time and check solution
main_test()
