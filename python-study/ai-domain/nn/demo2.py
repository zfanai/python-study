#encoding:utf8

import numpy as np
 
# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
 
# input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
 
# output dataset            
y = np.array([[0,0,1,1]]).T
 
# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)
 
# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1

print 'syn0:', syn0 , X
 
# L0是输入层
# 没有隐藏层
for iter in xrange(10000):
    # forward propagation
    L0 = X
    L1 = nonlin(np.dot(L0,syn0))
 
    # how much did we miss?
    L1_error = y - L1
 
    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    L1_delta = L1_error * nonlin(L1,True)
 
    # update weights
    syn0 += np.dot(L0.T,L1_delta)
    
print "Output After Training:"
print L1