import numpy as np
from numpy import array


class Regressor:
    def __init__(self, x, r):
        self.x = x
        self.r = r
        self.calculate_paramaters()


    def predict_y(self, xt):
        return self.parameters[1][0] * xt + self.parameters[0][0]

    def calculate_paramaters(self):
        self.parameters = np.zeros(shape=(2, 1))
        sum_r = sum(self.r)
        sum_r_x = sum([r * x for r, x in zip(self.r, self.x)])
        N = len(self.x)
        sum_x = sum(self.x)
        sum_x_2 = sum([x ** 2 for x in self.x])
        y = array([[sum_r], [sum_r_x]])
        A = array([[N, sum_x],[sum_x, sum_x_2]])
        self.parameters = np.matmul(np.linalg.inv(A), y)
