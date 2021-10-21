from scipy import io
import numpy as np
from scipy.io.matlab.mio5_utils import squeeze_element

'''     create file mat
arr = np.arange(10)
io.savemat('arr.mat',{'vec':arr})
'''

#Display all information
'''
#Export:
arr = np.array([0,1,2,3,4,5,6,7,8,9])
io.savemat('arr.mat',{'ver':arr})
#Import
mydata = io.loadmat('arr.mat')
print(mydata)
'''

#Display only the data
#Export:
arr = np.array([0,1,2,3,4,5,6,7,8,9])
io.savemat('arr_2.mat',{'vec':arr})
#Import
mydata = io.loadmat('arr_2.mat',squeeze_me=True)    # Return Array,not sqeeze_me return + 1 dimension
print(mydata['vec'])

