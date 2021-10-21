import matplotlib.pyplot as plt
import numpy as np

x = np.array([70, 75, 80, 85, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Title",color='r',fontdict={'color':'blue','size':'25'})
plt.xlabel('Nam',fontdict={'family':'Arial','color':'black','size':'15'},loc='right')
plt.ylabel('Nu',fontdict={'family':'serif','color':'black','size':'15'},loc='top')

plt.plot(x,y,"o--",ms=10,mfc='r')

plt.grid(axis='y',color='black',linestyle='--')
plt.show()