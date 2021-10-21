#Permutation: Hoan vi
from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])
#random.shuffle(arr)
#for x in range(10):
#    random.shuffle(arr)
#    print(arr)

#change original
arr = np.array([1,2,3,4,5])
print(random.permutation(arr))