#!/usr/bin/python

import numpy as np
def one_hot(labels, n_classes):
    o_h = np.zeros((len(labels), n_classes))
    for i in range(len(labels)):
        o_h[i, labels[i]] = 1.0
    return o_h



labels = [0,1,2,3,3,4,5,6]


x = one_hot(labels, 7)

print(x)

""" Expected result
[[ 1.  0.  0.  0.  0.  0.  0.]
 [ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]]
"""
