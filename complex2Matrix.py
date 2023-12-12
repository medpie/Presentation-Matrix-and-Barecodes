# Generating a dimension-sorted dictionary of simplices from a simplicial complex.
# Creating a list of simplices from a simplicial complex
# Creating the boundary matrix of a simplicial complex
# Plotting Persistence Diagram 
import matplotlib.pyplot as plt
import TDA_Ex as tdx
import numpy as np
from itertools import combinations
  

def listof_simplices(scomplex):
  simplices = []
  for s in scomplex:
     dim_s = len(s)
     for index in range(1,dim_s + 1):
        sim_index = [obj for obj in combinations(s, index)]
        simplices += sim_index
  return list(set(simplices))


#=========================================
def matrixof_simplices(scomplex):
  n = len(listof_simplices(scomplex))
  matrix = np.array([[0 for _ in range(n)] for _ in range(n)])
  for simplex in listof_simplices(scomplex):
     dim_simplex = len(simplex) - 1
     if dim_simplex > 0:
        j = listof_simplices(scomplex).index(simplex)
        lower_d = [obj for obj in combinations(simplex, dim_simplex)]
        for num in range(len(lower_d)):
           i = listof_simplices(scomplex).index(lower_d[num])
           matrix[i,j] = 1
  return matrix


#=============================================
#Persistence Diagram
def pers_diagram(scomplex):
     n = len(listof_simplices(scomplex))
     list = tdx.barcode(matrixof_simplices(scomplex), n, n)
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

#scomplex = [[1,2], [2,3,4]]
scomplex = [[1,2,3],[3,4],[4,5,6,7],[4,1],[4,1,8,11], [8,3,6,7,11], [11,7]]
print(listof_simplices(scomplex))
print(matrixof_simplices(scomplex))
pers_diagram(scomplex)
