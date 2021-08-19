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

    res_arr = []
    res_arr.append(res)

    print(f'Total: {len(res)}')
    
    q = pQueue.PriorityQueue()

    size = p.size
    heuristic = -1
    t = 0
    track_table = [0 for x in range(-size ** 2, size **2 + 1) if x != 0]
    while heuristic != 0:
        for i in range(size):
            for j in range(size):
                if p.board[i][j] in exclude_list and -p.board[i][j] in exclude_list:
                    continue
                point = p.board[i][j]
                k = [x for x in res_arr[t] if -p.board[i][j] in x] # clause thoa man am
                if len(k) > 0:
                    min_c = min([len(x) for x in k])
                    value = len(k)
                    if -p.board[i][j] not in exclude_list:
                        q.insert([-point, min_c * value , t, exclude_list[-1]])

                k2 = [x for x in res_arr[t] if p.board[i][j] in x] # clause thoa man duong
                if len(k2) > 0:
                    min_c2 = min([len(x) for x in k2])
                    value2 = len(k2)
                    if p.board[i][j] not in exclude_list:
                        q.insert([point, min_c2 * value2, t, exclude_list[-1]])
                #f(n)= g(n) + h(n)

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
            if t + 1 >= len(res_arr):
                res_arr.append([])
            res_arr[t + 1] = [x for x in res_arr[t] if key not in x]
            for it in res_arr[t + 1]:
                if -key in it:
                    it.remove(-key)
            t +=1 
            print(t)
                

        else:
            break
            
    print(track_table)
    for it in [x for x in range(-size **2, size ** 2 + 1) if x != 0]:
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