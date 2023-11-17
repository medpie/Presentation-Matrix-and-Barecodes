# Exercise 8.17, page 84, TDA book
import random
import numpy as np
import time as t
import pandas as pd

#Creating a pivot array for an m by n matrix
def pivot(x,m,n):
  #piv = np.full(n, None)
  piv = [None for _ in range(m)]
  for j in range(n):
    for i in range(m):
        if x[i][j] != 0:
          piv[j] = i+1
  return piv 

# Standard Reduction matrix with rightward Boolean column addition, i.e., F = Z/2Z
def standard_breduced(x, m, n):
            for j in range(n):
                   for k in range(j):
                       if pivot(x,m,n)[j] == pivot(x,m,n)[k] and pivot(x,m,n)[j] != None:
                           p = pivot(x,m,n)[j]
                           for i in range(m):
                               # For binary matrices
                               x[i][j] = (x[i][j] + x[i][k]) % 2
                               #x[i][j] = (- x[p-1][j]/x[p-1][k])*x[i][k] + x[i][j]
                           standard_breduced(x,m,n)
            return x 

# Standard Reduction matrix with rightward column addition, i.e., Field = Reals
def standard_reduced(x, m, n):
            for j in range(n):
                   for k in range(j):
                       if pivot(x,m,n)[j] == pivot(x,m,n)[k] and pivot(x,m,n)[j] != None:
                           p = pivot(x,m,n)[j]
                           for i in range(m):
                               # For binary matrices
                               #x[i][j] = (x[i][j] + x[i][k]) % 2
                               x[i][j] = (- x[p-1][j]/x[p-1][k])*x[i][k] + x[i][j]
                           standard_reduced(x,m,n)
            return x 



# Computing barecode of a reduced matrix x
def barcode(matrix, m, n):
  #Choose the type of standard reduction based on the abient field
  x = standard_breduced(matrix,m,n)
  barc = []
  for k in range(n):
    if (pivot(x,m,n)[k] != None) and (pivot(x,m,n)[k] < k+1):
          barc.append(f'[{pivot(x,m,n)[k]}, {k+1})')
    elif (pivot(x,m,n)[k] == None) and ((k+1)) not in pivot(x,m,n):
        barc.append(f'[{k+1}, infinity)')
  return barc





#matrix = [[random.randint(0,1) for _ in range(10)] for _ in range(10)]
#print(matrix)
#print(pivot(matrix,10,10))
#standard_breduced(matrix,10,10)
#print(pivot(matrix,10,10))
#print(barcode(matrix, 10,10))
