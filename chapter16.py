
import math
import numpy as np

#ex2
def my_ls_params(f, x, y):
    n = len(x)
    m = len(f)
    X = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            X[i, j] = f[j](x[i])
    
    XTX = np.dot(X.T, X)
    XTy = np.dot(X.T, y)
    
print("", beta)

#ex3

