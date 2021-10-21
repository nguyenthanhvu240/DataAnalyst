import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y,color='red',marker='o')


x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x,y,color='blue',marker='x')

plt.grid(axis='both',color='black',linestyle='--')
plt.show()

x = np.array([3,4,4,3])
y = np.array([85,70,90,110])
colors = np.array(['brown','gray','green','cyan'])
plt.scatter(x,y,c=colors)

plt.show()

#The Matplotlib module has a number of available colormaps.
# Day mau co san
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x, y, c=colors, cmap='nipy_spectral',s=sizes,alpha=0.5)

plt.colorbar()

plt.show()
