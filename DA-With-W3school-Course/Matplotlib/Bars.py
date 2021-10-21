import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
plt.xlabel("Letter")
y = np.array([3,8,1,10])
plt.ylabel("Number")
plt.bar(x,y,color='red',width=0.3)
plt.show()

#Horizontal Bars
x = np.array(["A","B","C","D"])
plt.xlabel("Number")
y = np.array([3,8,1,10])
plt.ylabel("Letter")
plt.barh(x,y,height=0.2)
plt.show()