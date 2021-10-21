import matplotlib.pyplot as plt
import numpy as np

"""
x1 = np.array([6,4,8,2])
y1 = np.array([3,8,1,10])

x2 = np.array([6,4,8,2])
y2 = np.array([6,2,7,9])

plt.plot(x1,y1,'X:r')

plt.plot(x2,y2,'g')
plt.show()
"""

x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
x2 = np.array([4,5,6,7])
y2 = np.array([6,2,7,11])
plt.plot(x1,y1,'o--r',x2,y2,'o:k')
plt.show()


