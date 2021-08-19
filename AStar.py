import Problem
import numpy as np
import priority_queue as pQueue

#def cost_function(arr, p2)


def solve(p):
    res = p.gen_all_CNF()
    
    exclude_list = [] # list chua phan tu xet roi
    pos=[x for x in res if sum(x) > 0]
    neg=[x for x in res if x not in pos]
    neg_arr = []
    pos_arr = []
    neg_arr.append(neg)
    pos_arr.append(pos)
    print(f'Total: {len(res)}')
    
    q = pQueue.PriorityQueue()

    size = p.size
    heuristic = -1
    path = [[]]
    t = 0
    while heuristic != 0:
        res_1 = []
        res_2 = []
        distance = []
        for i in range(size):
            for j in range(size):
                if p.board[i][j] not in exclude_list and p.board[i][j] not in path[t]:
                    point = p.board[i][j]
                    k = [x for x in neg_arr[t] if -p.board[i][j] not in x]
                    value = len(k)
                    res_1.append([point, value])
                    k2 = [x for x in pos_arr[t] if p.board[i][j] not in x]
                    #k2 = [list(np.delete(x, np.where(np.array(x) == point))) for x in pos]
                    #k2 = list(set(tuple(sorted(sub)) for sub in k2)) # remove duplicate
                    value2 = len(k2)
                    
                    if len(pos) > value2:
                        res_2.append([point, value2])
                    
                    if len(neg) > value:
                        q.insert([point, value])

        #distance = [[res_1[index][0], res_1[index][1] + res_2[index][1]] for index in range(len(res_1))]
        
        #distance = sorted(distance, key = lambda x : x[1])
        #res_1 = sorted(res_1, key = lambda x : x[1])
        #res_2 = sorted(res_2, key = lambda x : x[1])
        if (not q.isEmpty()):
            choose = q.delete()
            print(choose)
            key = choose[0]
            heuristic = choose[1]
            
            exclude_list.append(key)
            print(f'Chosen: {key} , heuristic: {heuristic}')
            if t + 1 >= len(neg_arr):
                neg_arr.append([])
                pos_arr.append([])
            neg_arr[t + 1] = ([x for x in neg_arr[t] if -key not in x])
            pos_arr[t + 1] = ([x for x in pos_arr[t] if key not in x])
            path[t].append(key)
            check = False
            print(pos_arr[t+1])
              
            if len(pos_arr[t+1]) == 0:
                check = True
                exclude_list.pop()
                
            print(path)
            if not check:
                t+=1
                if t >= len(path):
                    path.append([])
                    
            #        print(exclude_list)
            #       raise "Problem"
            #        break
        else:
            t -= 1
            

        
    #exclude_list.pop()
    print(exclude_list)
        
    solution = list()
    for x in range(1, size ** 2 + 1):
        if x in exclude_list:
            solution.append(-x)
        else:
            solution.append(x)
    


    return solution