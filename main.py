from backtrack import solve
from AStar import solve
from pysat import solve
from BruteForce import solve
import Problem

import time

def read_file(input_file):
    matrix = list()
    with open(input_file, 'r') as f:
        for line in f:
            matrix.append(line.split())    
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
    solution = solve(p)

    # Write into output file
    write_file('output.txt', solution)    


def main_test():
    matrix = read_file('../testcase/level-3-5-input.txt')

    # formualte problem
    p = Problem(matrix)
    
    # initialize
    duration = time.time() - time.time()
    count = 0
    # start clock

    # number of time to run
    max_run = 1
    for _ in range(max_run):
        print("Running: " + str(_ + 1)  + '...')
        
        start = time.time()

        # Your algorithma2

        solution = solve(p)

        # Should have a line: solution = ....

        # end clock
        end = time.time()    
        
        # print the interval + solution
        duration += end - start

        # Check: complete + leading number != 0
        if solution != None and p.check_solution(solution):
            count+=1 # count number of successful run 

    print("......................................")
    print(f'Solution: {solution}')
    print('>>>>>')
    print(f'Number of success solution: {count}/{max_run}')
    if solution != None:
        if p.check_solution(solution):
            print('Correct solution!')
        else:
            print('Wrong solution!')
    print('<<<<<<')
    print(f'Time require: {duration / max_run}')
    print("......................................")


#----------------------------------------------------------------------
# call main function
if __name__ == '__main__':
    main()

# Call main_test() if you want to show time and check solution
#main_test()
