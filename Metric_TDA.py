from itertools import permutations, combinations
import numpy as np

#Making a list of all matchings of k pairs (a,b) where a and b are intervals in A & B 
def matching(A,B,k):
    k_match = []
    M = [[[A[i], B[j]] for j in range(len(B))] for i in range(len(A))]
    k_indices = combinations([_ for _ in range(len(A))], k)
    for item in k_indices:
            perm = permutations([_ for _ in range(len(B))], k)
            for p in perm:
                  k_match.append([M[item[index]][p[index]] for index in range(k)])
    return k_match


#Computing Wasserstein distance of two barcodes (two lists of intervals)
def Wasserstein(A,B,p):
      if len(A) > len(B):
            A, B = B, A
      sum = []
      for k in range(1,len(A)+1):
            k_pairs = matching(A, B, k)
            sum_k = []
            for item in k_pairs:
                  sum_k_item = 0
                  for index in range(k):
                     sum_k_item += np.abs(item[index][0][0] - item[index][1][0])**p + np.abs(item[index][0][1] - item[index][1][1])**p
                  for B_item in B:
                        value = False
                        for index in range(k):
                                          if B_item == item[index][1]:
                                                 value = True
                        if value == False:
                               sum_k_item += 2*(((B_item[1] - B_item[0])/2)**p)
                  sum_k.append(sum_k_item)
            min_sum_k = min(sum_k)
            sum.append(min_sum_k)
      return f'Wasserstein Distance of A and B: {min(sum)}'                 

A = [[0,2],[4,7]]
B = [[0,7],[4,8]]
#print(matching(A,B, 2))
print(Wasserstein(A,B,1))

