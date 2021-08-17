import Problem
import numpy as np

def get_surrounding(matrix, i, j):
    size = len(matrix)
    result = []
    for y in range(-1, 2):
        result += [matrix[i + x][j + y] for x in  range(-1, 2) if 0 <= i + x < size and 0 <= j + y < size]
    return sorted(result)

def solve(p):
    res = p.gen_all_CNF()
    
    pos=[x for x in res if sum(x) > 0]
    neg=[x for x in res if x not in pos]
    for i in range(p.size):
        for j in range(p.size):
            if p.puzzle[i][j] == 0:
                for choose in get_surrounding(p.board, i , j):
                    neg = [x for x in neg if -choose not in x]
                    neg = list(set(tuple(sorted(sub)) for sub in neg)) # remove duplicate

                    pos = [x for x in pos if choose not in x]
            """
            if p.puzzle[i][j] == 6 and len(get_surrounding(p.board, i , j)) == 6:
                for choose in get_surrounding(p.board, i , j):                    
                    pos = [x for x in pos if choose not in x]
                    pos = list(set(tuple(sorted(sub)) for sub in pos)) # remove duplicate

                    neg = [x for x in neg if -choose not in x]
            """

            
    
    
         
    print(f'Total: {len(res)}')
    #for it in res:
    #    print(it)
    size = p.size
    heuristic = -1
    exclude_list = [] # list chua phan tu xet roi
    while heuristic != 0:
        res_1 = []
        res_2 = []
        for i in range(size):
            for j in range(size):
                if p.board[i][j] not in exclude_list:
                    point = p.board[i][j]
                    k = [x for x in neg if -p.board[i][j] not in x]
                    value = len(k)
                    res_1.append([point, value])
                    res_2.append((p.board[i][j], len([x for x in pos if p.board[i][j] not in x])))#, len([x for x in pos if p.board[i][j] in x]))))
        
        distance = [[res_1[index][0], min(res_1[index][1] , res_2[index][1]) ] for index in range(len(res_1))]
        
        distance = sorted(distance, key = lambda x : x[1])
        res_1 = sorted(res_1, key = lambda x : x[1])
        res_2 = sorted(res_2, key = lambda x : x[1])
        print(res_1)
        print(res_2)
       
        print(distance)
        index = 0
        while (index < len(distance) - 1 and distance[index][1] != 0 and distance[index][1] == distance[index + 1][1]):
            index+=1
            if index < len(distance) - 1 and distance[index][1] != distance[index + 1][1]:
                index += 1
        if distance[index][1] == distance[index - 1][1]:
            index = 0
        h = distance[index]
        
        heuristic = h[1]
        choose = h[0]
        #h2 = res_2[index]
        
        #if h2[1] < heuristic: 
        exclude_list.append(h[0])
        print(f'Chosen: {h[0]} , heuristic: {heuristic}')
        
        pos = [x for x in pos if choose not in x]
        pos = [list(np.delete(x, np.where(x == []))) for x in pos]
        pos = list(set(tuple(sorted(sub)) for sub in pos)) # remove duplicate

        neg = [x for x in neg if -choose not in x]
        
        print(len(pos))

        #heuristic = len(pos)
        #print(pos)

    #exclude_list.pop()
    print(exclude_list)
        
    solution = list()
    for x in range(1, size ** 2 + 1):
        if x in exclude_list:
            solution.append(-x)
        else:
            solution.append(x)
    


    return solution