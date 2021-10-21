import numpy as np

'''
f = open( 'file2.txt' ,'r')
l = []
l = np.array([ line.split(',') for line in f])
print(l)
print(type(l))
'''
data = np.loadtxt("./file2.txt",delimiter=",")
print("Shape of Array:",data.shape)
print("Read data From File:\n",data)


    
'''f = open("newfile.txt",'x')
f.write(str(data))'''

f = open("newfile.txt","r")
newf = f.read().replace(".","")
print(newf)
