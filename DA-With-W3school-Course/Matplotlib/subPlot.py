import matplotlib.pyplot as plt
import numpy as np


#plot 1:
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,1,1)
#the figure has 1 row, 2 columns, and this plot is the first plot.
plt.plot(x,y,marker='o',mfc='red')
plt.grid(axis='y')
plt.ylabel('NAM')

#plot 2:
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,1,2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
plt.plot(x,y)
plt.grid(axis='y')
plt.ylabel('NỮ')

#So, if we want a figure with 2 rows an 1 column (meaning that the two plots will be displayed on top of each other instead of side-by-side), we can write the syntax like this:
plt.suptitle('Gioi Tinh')
plt.show()

#==================================================
x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x1,y1,marker='o',mfc='red',ms=10,color='black')
plt.title('NAM')
plt.grid(axis='y')

x2 = np.array([0,1,2,3])
y2 = np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x2,y2)
plt.title('NU')
plt.grid(axis='y')

plt.suptitle('GIOITINH')
plt.show()



