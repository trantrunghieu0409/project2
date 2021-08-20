def solve(p, app):
    res = p.gen_all_CNF()
    size = p.size
    heuristic = -1
    exclude_list = [] # list chua phan tu xet roi
    countStep = 1
    while heuristic != 0:
        res_1 = dict()
        for i in range(size):
            for j in range(size):
                if p.board[i][j] in exclude_list:
                    continue
                elif -p.board[i][j] in exclude_list:
                    continue
                else:
                    for x in res:
                        if p.board[i][j] in x:
                            if -p.board[i][j] in res_1:
                                res_1[-p.board[i][j]][1] += 1
                            if p.board[i][j] in res_1:
                                if res_1[p.board[i][j]][0] > len(x):
                                    res_1[p.board[i][j]][0] = len(x)
                                res_1[p.board[i][j]][1] -= 1 # use the number of time it occur to a second heuristic
                            else:
                                res_1[p.board[i][j]] = [len(x), -1]
                        elif -p.board[i][j] in x:
                            if p.board[i][j] in res_1:
                                res_1[p.board[i][j]][1] += 1
                            if -p.board[i][j] in res_1:
                                if res_1[-p.board[i][j]][0] > len(x):
                                    res_1[-p.board[i][j]][0] = len(x)
                                res_1[-p.board[i][j]][1] -= 1 # use the number of time it occur to a second heuristic
                            else:
                                res_1[-p.board[i][j]] = [len(x), -1]
                        else:
                            if sum(x) > 0:
                                if p.board[i][j] in res_1:
                                    res_1[p.board[i][j]][1] -= 1
                            elif sum(x) < 0:
                                if -p.board[i][j] in res_1:
                                    res_1[-p.board[i][j]][1] -= 1
        if len(res_1) == 0:
            break
        key = min(res_1, key=res_1.get)
        heuristic = res_1[key][0]
        if heuristic > 0:
            exclude_list.append(key)
            res = [x for x in res if key not in x]
            for y in res:
                if -key in y:
                    y.remove(-key) 
        if key < 0:
            app.update_square((abs(key)-1)//size, (abs(key)-1) % size, size, heuristic, countStep, app.red)
            countStep += 1

    solution = [x if x in exclude_list else -x for x in range(1, size ** 2 + 1)]

    return solution