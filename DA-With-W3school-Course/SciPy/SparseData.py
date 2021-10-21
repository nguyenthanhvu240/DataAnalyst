#CSC - Comlumn
#CSR - Row

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr)) 
#The 1. item is in row 0 position 5 and has the value 1.
#The 2. item is in row 0 position 6 and has the value 1.
#The 3. item is in row 0 position 8 and has the value 2.

print(csr_matrix(arr).data)     #>not include value 0

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)     #>not include value 0

arrr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arrr).count_nonzero())

#Remove zero-entries
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

#Converting from csr to csc with the tocsc() method
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

newarr = csr_matrix(arr).tocsc()

print(newarr)