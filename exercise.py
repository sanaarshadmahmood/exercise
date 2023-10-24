# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:22:33 2023

@author: SANA
"""

import numpy as np
x=np.array([3,4,6,10,24,89,45,43,46,99,100])
print(x[x%3==0])
print(x[x%5==0])
print(x[(x%3==0) &( x%5==0)])
x[x%3==0] =42

print(x)

A = np.array([[3, 1, 5, 3, 7],
              [8, 2, 5, 9, 2],
              [8, 5, 1, 0, 3],
              [9, 1, 6, 1, 5],
              [5, 7, 4, 1, 6]])

A[::2, :] = 10
print(A)

A = np.array([[4, 6, 7, 2],
              [5, 1, 9, 2]])

print(A.argmin())

A = np.ones((2, 4), dtype=int)
B = np.arange(4)
C = A + B
print(C)
print(C[-1, -2])