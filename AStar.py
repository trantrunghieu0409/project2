import Problem
import numpy as np
import priority_queue as pQueue

#def cost_function(arr, p2)
def find_way(track_table, end_point):
    index = -1
    path = []
    size = len(track_table) // 2
    while index == -1 or track_table[index] != 0:
        if end_point < 0:
            index = abs(end_point) - 1
        elif end_point > 0:
            index = size + end_point - 1
        end_point = track_table[index]
        path.append(end_point)
    return path



def solve(p):
    res = p.gen_all_CNF()
    
    exclude_list = [0] # list chua phan tu xet roi
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
    t = 0
    track_table = [0 for x in range(-size ** 2, size **2 + 1) if x != 0]
    while heuristic != 0:
        res_1 = []
        res_2 = []
        res_3 = []
        res_4 = []
        distance = []
        for i in range(size):
            for j in range(size):
                if p.board[i][j] in exclude_list and -p.board[i][j] in exclude_list:
                    continue
                point = p.board[i][j]
                k = [x for x in neg_arr[t] if -p.board[i][j] not in x]
                value = len(k)
                k2 = [x for x in pos_arr[t] if p.board[i][j] not in x]
                value2 = len(k2)
                
                if -p.board[i][j] not in exclude_list:
                    q.insert([-point, value + len(pos_arr[t]) - value2 , t, exclude_list[-1], value])

                if p.board[i][j] not in exclude_list:
                    q.insert([point, len(neg_arr[t]) - value + value2, t, exclude_list[-1], value2])
        #print(sorted(q.queue, key = lambda x : x[1]))

        if (not q.isEmpty()):
            choose = q.delete()
            
            key = choose[0]
            heuristic = choose[1]
            t = choose[2]
            index = 0
            if key > 0:
                index += p.size
            track_table[index + abs(key) - 1] = choose[3]
            exclude_list.append(key)
            print(f'Chosen: {key} , heuristic: {choose[1]}')
            if t + 1 >= len(neg_arr):
                neg_arr.append([])
                pos_arr.append([])
            if key < 0:
                neg_arr[t + 1] = ([x for x in neg_arr[t] if key not in x])
                pos_arr[t + 1] = ([x for x in pos_arr[t]])
            else:
                pos_arr[t + 1] = ([x for x in pos_arr[t] if key not in x])
                neg_arr[t + 1] = ([x for x in neg_arr[t]])
            t +=1 
            print(t)
                

        else:
            break
            
    print(track_table)
    for it in [x for x in range(-size **2, 0) if x != 0]:
        print(it)
        solution = [it]
        b = find_way(track_table, it)
        solution.extend(b)
        solution.pop() 
        a = solution.copy()  
        solution = [x for x in range(1, size ** 2 + 1)]
        for it in a:
            solution[abs(it) - 1] = int(it)
        print(solution)


        if (p.check_solution(solution)):
            raise "congraluation!!!!!!!!!!!!!!"
        p.show(solution)
    #exclude_list.pop()
    print(exclude_list)
        
    


    return solution