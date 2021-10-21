import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(0,5,250)
#print(x)
plt.hist(x,10)
"""We use the array from the example above to draw a histogram with 5 bars.
The first bar represents how many values in the array are between 0 and 1.
The second bar represents how many values are between 1 and 2.
"""
plt.show()

