import numpy as np
from numpy import array


class PCA:
    def __init__(self, data):
        self.data = data
        self.cov_of_data = np.cov(self.data)
        self.mean = np.mean(data, axis=0)
        w = np.linalg.eig(self.cov_of_data)[1]
        first_component = w[:, 0]
        second_component = w[:, 1]
        self.w = array([[first_component[0], second_component[0]], [first_component[1], second_component[1]],
                        [first_component[2], second_component[2]]])

    def reduce_dimentionality(self, instance):
        z = np.matmul(self.w.T, instance - self.mean)
        return z

    def increase_dimentionality(self, projected_data):
        x_reconstructed = np.matmul(self.w,projected_data) + self.mean
        return x_reconstructed
