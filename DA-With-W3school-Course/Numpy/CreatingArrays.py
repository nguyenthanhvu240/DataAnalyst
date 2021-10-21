import numpy as np
from numpy.testing._private.utils import HAS_REFCOUNT

arr = np.array([1,2,3,4,5])
print(type(arr))
print(arr.ndim)

#convert a tuple to array
arr = np.array((1,2,3,4,5))
print(arr)
print(arr.ndim)

#Scarlar (0-D) : vo huong
arr = np.array(111)
print(arr)
print(arr.ndim)

#2-D
arr = np.array(
    [[1,2,3],
    [4,5,6]])
print(arr)
print(arr.ndim)

#3-D
arr = np.array(
    [[[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]])
print(arr)
print(arr.ndim)

#Create N-dim
arr = np.array([1,2,3,4],ndmin=4)
print(arr)
print("Number of dimensions:",arr.ndim)