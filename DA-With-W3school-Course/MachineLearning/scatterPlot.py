import numpy as np
import matplotlib.pyplot as plt

#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]  #age
#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]  #speed
#plt.scatter(x,y)
#plt.show()

####### RANDOM DATA DISTRIBUTION
x = np.random.normal(5,1,1000)
y = np.random.normal(10,2,1000)
plt.scatter(x,y)
plt.show()