import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([1,8])
ypoint = np.array([3,10])
plt.plot(xpoint,ypoint)
plt.show()

#@To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
xpoint2 = np.array([1,8])
ypoint2 = np.array([3,10])
plt.plot(xpoint2,ypoint2,'o')
plt.show()

#@Multiple Points
#You can plot as many points as you like, just make sure you have the same number of points in both axis.


xpoint3 = np.array([1,2,6,8])
ypoint3 = np.array([3,8,6,10])
plt.plot(xpoint3,ypoint3)
plt.show()

#@Default X-points
#If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.
xpoint4 = np.array([3,8,1,10,5,7])
plt.plot(xpoint4)
plt.show()
