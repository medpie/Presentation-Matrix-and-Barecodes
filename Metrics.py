import numpy as np
import random
import matplotlib.pyplot as plt

def dist(I, J, r):
  distance, list2 = 0, []
  for i in range(len(I)):
    for j in range(len(J)):
            if np.abs(I[i][0] - J[j][0]) <= r and np.abs(I[i][1] - J[j][1]) <= r:
              distance += np.abs(I[i][0] - J[j][0]) + np.abs(I[i][1] - J[j][1])
            else:
               distance += 2*np.abs(I[i][0] - (I[i][0] + I[i][1])/2) + 2*np.abs(J[j][0] - (J[j][0] + J[j][1])/2)
  return distance  
        
def Wasserstein_delta(I, J):
   max_delta = max([max([I[_][0] for _ in range(len(I))]), max([I[_][1] for _ in range(len(I))]), max([J[_][0] for _ in range(len(J))]), max([J[_][1] for _ in range(len(J))])])
   distances = [dist(I, J, r) for r in range(1, max_delta + 1)]
   index = distances.index(min(distances))
   return index + 1

x = [[random.randint(0,30), random.randint(0,30)] for _ in range(random.randint(1,30))]
print(f'Barcode1: {x}')
y = [[random.randint(0,30), random.randint(0,30)] for _ in range(random.randint(1,30))]
print(f'Barcode2: {y}')
R = [_ for _ in range(30)]
Dist = [dist(x,y,R[_]) for _ in range(30)]
plt.scatter(R, Dist) 
plt.show()

print(f'Wasserstein distance = {min(Dist)},  delta = {Wasserstein_delta(x,y)}')




      
          
