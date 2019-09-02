import numpy as np
from numpy import linalg as la
from math import *

# approximated entropy of particle-approximated pdf
def entropy(x_s, w_s = None):
    dim = x_s.shape[0]
    C = np.cov(x_s, aweights = w_s)
    entropy = 0.5 * la.det(C) + 0.5 * dim * (1 + log(2*pi))
    return entropy

def multi_gaussian_entropy(tmp = None):
    # see Huber, Marco F., et al. "On entropy approximation for Gaussian mixture random vectors." 2008 IEEE International Conference on Multisensor Fusion and Integration for Intelligent Systems. IEEE, 2008.
    # or http://www-personal.acfr.usyd.edu.au/tbailey/publications/gmmentropybounds.htm
    raise NotImplementedError


if __name__=='__main__':
    N = 10000
    x_s = np.random.randn(2, N)
    w_s = np.ones(N)*1.0/N
    sol_numerilcal = entropy(x_s, w_s)
    sol_analytical = 0.5 * 1 + 0.5 * 2 * (1 + log(2*pi))
    print sol_numerilcal - sol_analytical


