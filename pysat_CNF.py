import Problem
from pysat.solvers import Glucose3

def solve(p):
    CNF_clauses = p.gen_all_CNF()
    CNF_clauses.append([33])

    g = Glucose3()
    for it in CNF_clauses:
        g.add_clause([int(k) for k in it])
    g.solve()
    model = g.get_model()
    return model
