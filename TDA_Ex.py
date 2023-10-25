# Exercise 8.17, page 84, TDA book
import random
import numpy as np
import time as t
import pandas as pd

def pivot(x,m,n):
  piv = np.full(n, None)
  for j in range(n):
    for i in range(m):
        if x[i][j] != 0:
          piv[j] = i+1
  return piv 

def standard_reduced(x, m, n):
            for j in range(n):
                   for k in range(j):
                       if None != pivot(x,m,n)[j] == pivot(x,m,n)[k] and pivot(x,m,n)[j]:
                           for i in range(m):
                               x[i][j] = (x[i][j] + x[i][k]) % 2
                           standard_reduced(x,m,n)
            return x 

values = []

for dim in range(5,30,5):
  a = t.time()
  matrix = [[random.randint(0,1) for _ in range(dim)] for _ in range(dim)]
  #matrix = [[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [1, 0, 0, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 1]]
  #print(matrix)
  #print(f'Pivots of the original matrix: {pivot(matrix, dim,dim)}')
  reduced_matrix = standard_reduced(matrix,dim,dim)
  #print(reduced_matrix)
  print(f'Pivots of the reduced matrix of dimension {dim}*{dim}: {pivot(reduced_matrix, dim,dim)}')
#print(len(set(pivot(matrix,10,10))))            
  b=t.time()
  values.append([f'{dim}*{dim}', f'{round((b-a)*1000, 2)} ms'])

dictionary = dict(zip([_ for _ in 'ABCDE'],values))
df = pd.DataFrame(dictionary)
labels = ['Dimesnion', 'Runtime']
df.index = labels
print(df) 




