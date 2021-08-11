import Problem
import itertools

def solve(p):
    CNF_clauses = p.gen_all_CNF()
    print(brute_force(CNF_clauses))

def brute_force(cnf):
    literals = set()
    lst = []
    for conj in cnf:
        lst.append(set(conj))
        for disj in conj:
            literals.add(disj)

    print(lst)
    result = set()
    for it in lst:
        result = set.union(it, result)
        # result = set(result).intersection(it)

    print(result)