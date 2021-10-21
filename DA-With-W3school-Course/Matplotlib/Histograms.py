import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(170,10,250) #250 values,around 170,deviation 10
plt.hist(x)
plt.show()