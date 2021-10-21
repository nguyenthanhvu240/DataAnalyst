import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([230, 220, 210, 250, 290, 240, 300, 350, 310, 340])

plt.plot(x,y)
fontx = {'family':'serif','color':'red','size':'20'}    #dictionary
fonty = {'family':'Arial','color':'yellow','size':'20'}     #dictionary

plt.title("GioiTinh",color='green',fontdict={'size':'25'})
plt.xlabel("Nam",color='r',fontdict=fontx,loc='right')
plt.ylabel("Nu",color='hotpink',fontdict=fonty,loc='top')

plt.show()
