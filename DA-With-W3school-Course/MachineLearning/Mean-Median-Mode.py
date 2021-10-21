import numpy as np

#MEAN   : SUM/Number of values
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
print(x)

#MEDIAN : sort the array and find the middle
y = np.median(speed)
print(y)

#MODE : the value that appears the most
from scipy import stats
z = stats.mode(speed)
print(z)