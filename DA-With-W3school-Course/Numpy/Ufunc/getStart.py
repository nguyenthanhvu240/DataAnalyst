import numpy as np
x = [1,2,3,4]
y = [5,6,7,8]
z = []
for i,j in zip(x,y):
    z.append(i+j)
print(z)

x = [1,2,3,4]
y = [5,6,7,8]
z = np.add(x,y)
print(z)