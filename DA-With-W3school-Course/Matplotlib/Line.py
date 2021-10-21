import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([3,8,1,10])
plt.plot(ypoint,'r') #dashed
plt.show()

#Line width
ypoint2 = np.array([3,8,1,10])
plt.plot(ypoint2,'r',linewidth='5')
plt.show()

