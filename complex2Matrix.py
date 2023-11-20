# Generating a dimension-sorted dictionary of simplices from a simplicial complex.
# Creating a list of simplices from a simplicial complex
# Creating the boundary matrix of a simplicial complex
# Plotting Persistence Diagram 
import matplotlib.pyplot as plt
import TDA_Ex as tdx

def complex_dimension(scomplex):
   return max([len(scomplex[i])-1 for i in range(len(scomplex))])

def dict_simplices(scomplex):
  n = sum(len(scomplex) for i in range(len(scomplex)))
  dimension = complex_dimension(scomplex)
  vertices = []
  for i in range(len(scomplex)):
    for j in range(len(scomplex[i])):
      vertices.append(scomplex[i][j])
  vertices = list(set(vertices))
  
  #organizing d-dimensional simplieces 
  keys = [_ for _ in range(dimension + 1)]
  values = [[] for _ in range(dimension + 1)]
  values[0] = [[_] for _ in vertices]
  simplices = dict(zip(keys,values))

  for i in range(len(scomplex)):
    dim = len(scomplex[i]) - 1
    for j in range(1, dim + 1):
       for s in combinations(scomplex[i], j + 1):
          values[j].append(s)  
  return simplices
  

def listof_simplices(scomplex):
  n = sum(len(scomplex) for i in range(len(scomplex)))
  dimension = complex_dimension(scomplex)
  vertices = []
  for i in range(len(scomplex)):
    for j in range(len(scomplex[i])):
      vertices.append(scomplex[i][j])
  vertices = list(set(vertices))
  
  #organizing d-dimensional simplieces 
  simplices = [[vertices[_]] for _ in range(len(vertices))]

  for i in range(len(scomplex)):
    dim = len(scomplex[i]) - 1
    for j in range(1, dim + 1):
       for s in combinations(scomplex[i], j + 1):
          simplices.append(s)  
  return simplices



def combinations(arr, k):
    result = []
    def nCk_list(current_combination, start_index):
        if len(current_combination) == k:
            result.append(current_combination[:])
            return
        for i in range(start_index, len(arr)):
            current_combination.append(arr[i])
            nCk_list(current_combination, i + 1)
            current_combination.pop()
    nCk_list([], 0)
    return result


def matrixof_simplices(scomplex):
  n = len(listof_simplices(scomplex))
  dim = complex_dimension(scomplex)
  matrix = [[0 for _ in range(n)] for _ in range(n)]
  for simplex in listof_simplices(scomplex):
     dim_simplex = len(simplex) - 1
     if dim_simplex > 0:
        j = listof_simplices(scomplex).index(simplex)
        lower_d = combinations(simplex, dim_simplex)
        for _ in range(len(lower_d)):
           i = listof_simplices(scomplex).index(lower_d[_])
           matrix[i][j] = 1

  return matrix

#Persistence Diagram
def pers_diagram(scomplex):
     n = len(listof_simplices(scomplex))
     list = tdx.bar(matrixof_simplices(scomplex), n, n)
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
     plt.show()
  
  
     
     


#scomplex = [[1,2,3],[3,4],[4,5,6,7],[4,1]]
scomplex = [[1,2],[1,3],[2,3,4],[4,5],[4,6],[5,6],[6,7]]
#scomplex = [[1,2,3]]
#print(dict_simplices(scomplex))
n = len(listof_simplices(scomplex))
#print(listof_simplices(scomplex).get(3))
#print(tdx.standard_breduced(matrixof_simplices(scomplex), n, n))
#print(tdx.pivot(matrixof_simplices(scomplex), n,n))
#x = matrixof_simplices(scomplex)
#y = tdx.standard_breduced(x, n,n)
#z = tdx.pivot(y, n,n)
#print(z)
#print(tdx.bar(matrixof_simplices(scomplex),n,n))
#print(tdx.barcode(matrixof_simplices(scomplex),n,n))
#print(pers_diagram(scomplex))
pers_diagram(scomplex)



