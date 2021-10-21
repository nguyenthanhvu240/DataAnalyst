import matplotlib.pyplot as plt
import numpy as np

y = np.array([10,10,30,50]) #counterclockwise : nguoc chieu kim dong ho
mylabel = [1,2,'three','four']

plt.pie(y,labels=mylabel)
plt.show()

plt.pie(y,labels=mylabel,startangle=90) #truc toa do
plt.show()

plt.pie(y,labels=mylabel,explode=[0.2,0,0.6,0],shadow=True)
plt.legend(title='Color')
plt.show()

