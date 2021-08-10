import numpy as np
class Problem:
    matrix = list(list())

    def __init__(self, matrix):
        self.matrix = [x[:] for x in matrix]

    def input(self):
        """
        return a copy of matrix 
        """
        return [x[:] for x in self.matrix]
    
    def check_solution(self, solution):
        pass

    def show(self, solution):
        """
        Visualize solution
        """
        pass