import numpy as np
import scipy.linalg as lag
hil10 = lag.hilbert(10)
hil10eig, eigenvectors = lag.eigh(hil10)
print("The array is", hil10eig)
print("K is", np.max(hil10eig)/np.min(hil10eig))
print("Max:", np.max(hil10eig))
print("Max:", np.min(hil10eig))
hil10inv = lag.inv(hil10)
product = hil10inv @ hil10
print("Inv*hil", product)
error = np.absolute(product - np.identity(10))
print("Max error is:", np.max(error))
hil10inv2 = eigenvectors @ np.reciprocal(hil10eig) @ np.transpose(eigenvectors)
product2 = hil10inv2 @ hil10
error2 = np.absolute(product2 - np.identity(10))
print("Max error is:", np.max(error2))
