import numpy as np
from numpy import array

class MultiVariate:
    def __init__(self, data_matrix):
        self.data = array(data_matrix)

    def get_mean_vector(self):
        return np.mean(self.data,axis=0)

    def get_covariance_matrix(self):
        return np.cov(self.data)