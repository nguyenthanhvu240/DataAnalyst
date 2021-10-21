import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
    print(x)


arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print("x represents the 2-D array:")
  print(x)
##############

arr = np.array([1,2,3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

##########
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

