# Generating a dimension-sorted dictionary of simplices from a simplicial complex.
# Creating a list of simplices from a simplicial complex
# Creating the boundary matrix of a simplicial complex
# Plotting Persistence Diagram 
import matplotlib.pyplot as plt
import TDA_Ex as tdx
import numpy as np
from itertools import combinations

# List of simplices
def listof_simplices(scomplex):
  simplices = set([comb for sim in scomplex for index in range(1,len(sim) + 1) for comb in combinations(sim, index)])
  return sorted(list(simplices), key = len)

#dictionary of simplices with keys = dimensions
def dictof_simplices(scomplex):
  simplices = listof_simplices(scomplex)   
  key = [dim for dim in range(max([len(sim) for sim in scomplex]))] # dimensions of simplices
  value = [[] for _ in range(len(key))]
  for item in simplices:
     index = len(item) - 1
     value[index].append(item)
  return dict(zip(key,value))



#=========================================
def matrixof_simplices(scomplex):
  dic = dictof_simplices(scomplex)
  dimension = max(dic.keys())
  allSimplices = [sim for k in range(dimension + 1) for sim in dic[k]]
  n = len(allSimplices)
  matrix = np.array([[0 for _ in range(n)] for _ in range(n)])
  key = 1
  while key <= dimension:
   for simplex in dic[key]:
      j = allSimplices.index(simplex)
      for lower_d in dic[key -1]:
         i = allSimplices.index(lower_d)
         if set(lower_d).issubset(simplex) == True:
           matrix[i,j] = 1
   key += 1
   if key == dimension + 1:
      break
  return matrix       


#print(dictof_simplices(scomplex))
#print(matrixof_simplices(scomplex))

#=============With Clearing

def Cmatrixof_simplices(scomplex):
  dic = dictof_simplices(scomplex)
  dimension = max(dic.keys())
  allSimplices = [sim for k in range(dimension + 1) for sim in dic[k]]
  n = len(allSimplices)
  matrix = np.array([[0 for _ in range(n)] for _ in range(n)])
  key = 1
  while key <= dimension:
   for simplex in dic[key]:
      j = allSimplices.index(simplex)
      row_counter = 0
      for lower_d in dic[key -1]:
         i = allSimplices.index(lower_d)
         if set(lower_d).issubset(simplex) == True:
           matrix[i,j] = 1
           row_counter = allSimplices.index(lower_d)
      if row_counter != 0:
         matrix[:,row_counter] = 0
   key += 1
   if key == dimension + 1:
      break
  return matrix       

#scomplex = [[1,2,3], [3,4], [2,5,7,8,9], [7,8,10], [3,6,7,8,9,10]]
#scomplex = [[1,2,3]]
#print(Cmatrixof_simplices(scomplex))

#=============================================
#Persistence Diagram
def pers_diagram(scomplex):
     dic = dictof_simplices(scomplex)
     dimension = max(dic.keys())
     allSimplices = [sim for k in range(dimension + 1) for sim in dic[k]]
     n = len(allSimplices)
     list = tdx.barcode(Cmatrixof_simplices(scomplex), n, n)
     x, y = [], []
     for point in list:
        if len(point) == 2:
           x.append(point[0])
           y.append(point[1])
        else:
           point.append(n)
           x.append(point[0])
           y.append(n+3)
     plt.scatter(x,y)
     plt.plot([0,n], [0,n], '--')
     plt.xticks(range(1,n+1))
     plt.yticks(range(1,n+1))
     plt.title('Persistence Diagram')
     plt.text(0, n+4, '--infinity--', fontsize=10, color='red')
     plt.text(2, 0, f'Complex: {scomplex}' , fontsize=10, color='green')
     plt.savefig('D:\\figure.jpg', format = 'png', dpi = 300)
     plt.show()

scomplex = [[1,2], [3,4,10], [2,5,7,8,9], [3,7,8,10], [3,6,7,8,9,10]]
#x = [comb for sim in scomplex for index in range(1,2) for comb in combinations(sim, index)]
pers_diagram(scomplex)
