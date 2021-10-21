import matplotlib.pyplot as plt
import numpy as np

#with lines
ypoint = np.array([3,8,1,10])
plt.plot(ypoint)    
plt.show()

#with marks
ypoint2 = np.array([3,8,1,10])
plt.plot(ypoint2,'o')   
plt.show()

#mark each point with *
ypoint3 = np.array([3,8,1,10])
plt.plot(ypoint3,marker='p')   
""" EX:
        '*'	Star	
        '.'	Point	
        ','	Pixel	
        'x'	X	
        'X'	X (filled)	
        '+'	Plus	
        'P'	Plus (filled)	
        's'	Square	
        'D'	Diamond	
        'd'	Diamond (thin)	
        'p'	Pentagon	
        'H'	Hexagon	
        'h'	Hexagon	
        'v'	Triangle Down	
        '^'	Triangle Up	
        '<'	Triangle Left	
        '>'	Triangle Right	
        '1'	Tri Down	
        '2'	Tri Up	
        '3'	Tri Left	
        '4'	Tri Right	
        '|'	Vline	
        '_'	Hline
"""
plt.show()

#Format String fmt
#You can use also use the shortcut string notation parameter to specify the marker.
#This parameter is also called fmt, and is written with this syntax:
#marker|line|color

ypoint4 = np.array([3,8,1,10])
plt.plot(ypoint4,'o:b',marker='X') # "-,:,--,-."
plt.show()

#Marker Size
ypoint5 = np.array([3,8,1,10])
plt.plot(ypoint5,marker='o',ms=10)
plt.show()

#Marker(Cover) Color
ypoint6 = np.array([3,8,1,10])
plt.plot(ypoint6,marker='o',ms=10,mec='r')
plt.show()

#Marker full color
ypoint7 = np.array([3,8,1,10])
plt.plot(ypoint7,'o--r',ms=15,mfc='hotpink')
plt.show()

