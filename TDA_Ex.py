# Exercise 8.17, page 84, TDA book
import random
import numpy as np

#Creating a pivot array for an m by n matrix
def pivot(x,m,n):
  piv = np.zeros(m)
  for j in range(n):
    for i in range(m):
        if x[i,j] != 0:
          piv[j] = i+1
  return piv 

#==================================
# Standard Reduction matrix with rightward Boolean column addition, i.e., F = Z/2Z
def standard_breduced(x, m, n):
            def column_operations(matrix, m, n):    
              for j in range(n):
                    for k in range(j):
                        if pivot(matrix,m,n)[j] == pivot(matrix,m,n)[k] and pivot(matrix,m,n)[j] != 0:
                                matrix[:, j] = (matrix[:, j] + matrix[:, k])%2
                               #x[i][j] = (- x[p-1][j]/x[p-1][k])*x[i][k] + x[i][j]
              return matrix
            while True:     
                  column_operations(x, m, n)
                  non_zero_piv = pivot(x,m,n)[pivot(x,m,n) != 0]
                  if len(non_zero_piv) == len(set(non_zero_piv)):
                       break
            return x 

matrix = np.array([[random.randint(0,1) for _ in range(20)] for _ in range(20)])
#print(matrix)
#print(pivot(matrix, 10,10))
#print(standard_breduced(matrix, 50, 50))
#print(pivot(standard_breduced(matrix, 20, 20), 20, 20))
#sample = standard_breduced(matrix, 50,50)
#np.savetxt('D:\\sample_text.txt', sample)


#======================================================================
# Standard Reduction matrix with rightward column addition, i.e., Field = Reals
def standard_reduced(x, m, n):
            def column_operations(matrix, m, n):    
              for j in range(n):
                    for k in range(j):
                        if pivot(matrix,m,n)[j] == pivot(matrix,m,n)[k] and pivot(matrix,m,n)[j] != 0:
                                p = pivot(x,m,n)[j]
                                x[:, j] = (- x[p-1,j]/x[p-1,k])*x[:, k] + x[:,j]
              return matrix
            while True:     
                  column_operations(x, m, n)
                  non_zero_piv = pivot(x,m,n)[pivot(x,m,n) != 0]
                  if len(non_zero_piv) == len(set(non_zero_piv)):
                       break
            return x
                           

#=======================================================
# Computing barecode of a reduced matrix x
def bar(matrix, m, n):
  #Choose the type of standard reduction based on the abient field
  x = standard_breduced(matrix,m,n)
  barc = []
  for k in range(n):
    if (pivot(x,m,n)[k] != 0) and (pivot(x,m,n)[k] < k+1):
          barc.append(f'[{pivot(x,m,n)[k]}, {k+1})')
    elif (pivot(x,m,n)[k] == 0) and ((k+1) not in pivot(x,m,n)):
        barc.append(f'[{k+1}, infinity)')
  return barc


#==================================================================
def barcode(matrix, m, n):
  #Choose the type of standard reduction based on the abient field
  x = standard_breduced(matrix,m,n)
  barc = []
  for k in range(n):
    if (pivot(x,m,n)[k] != 0) and (pivot(x,m,n)[k] < k+1):
          barc.append([pivot(x,m,n)[k], k+1])
    elif (pivot(x,m,n)[k] == 0) and ((k+1) not in pivot(x,m,n)):
        barc.append([k+1])
  return barc


print(barcode(matrix, 20, 20))
#=======================================================================



# Making a table of square matrix dimensions and their reduction runtimes
"""
data = [[random.randint(0,1) for _ in range(10)] for _ in range(10)]
x = [[np. for _ in range(10)] for _ in range(10)]
print(standard_reduced(data,10,10))
print(pivot(data,10,10))

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
df.index = ['Dimesnion', 'Runtime']
print(df) 
"""




