
# input: datamatrix as loaded by numpy.loadtxt('shapes.txt')
# output:  1) the eigenvalues in a vector (numpy array) in descending order
#          2) the unit eigenvectors in a matrix (numpy array) with each column being an eigenvector (in the same order as its associated eigenvalue)
#
# note: make sure the order of the eigenvalues is descending, and the eigenvectors have the same order as their associated eigenvalues

import numpy
import math

datamatrix = numpy.loadtxt('shapes.txt')

def pca(data):
    
    mean = numpy.mean(data, axis=1)
    
    for i in range(40):
        data[:,i] = data[:,i] - mean
    
    dtcov = numpy.cov(data)
    
    evals, evecs = numpy.linalg.eig(dtcov)
    real_evals = numpy.real(evals)
    real_evecs = numpy.real(evecs)
    
    #need to sort:
    idx = real_evals.argsort()[::-1]   
    real_evals = real_evals[idx]
    real_evecs = real_evecs[:,idx]

    
    return(real_evals, real_evecs)
    
print(pca(datamatrix))
