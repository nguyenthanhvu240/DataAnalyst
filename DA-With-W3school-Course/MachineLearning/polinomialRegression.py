import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

import numpy as np
#NumPy has a method that lets us make a polynomial model:
mymodel = np.poly1d(np.polyfit(x,y,3))
#Then specify how the line will display, we start at position 1, and end at position 22:
myline = np.linspace(1,22,100)

plt.scatter(x, y)
#Draw the line of polynomial regression:
plt.plot(myline,mymodel(myline))
plt.show()

###############
from sklearn.metrics import r2_score
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))