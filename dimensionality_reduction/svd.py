# Exhibiting X*X.T = V*E*V.T
import numpy as np
from numpy import array

def spectral_decomposition(X):
    X = array(X)
    print(np.matmul(X,X.T))
    cov_X = np.cov(X)
    eigen_results = np.linalg.eig(cov_X)
    v = eigen_results[1]
    e = np.diag(eigen_results[0])
    print(np.matmul(np.matmul(v,e),v.T)) # Verify the answer once. It is resulting in a matrix with all 1