from numpy import random
x = random.randint(100)
print(x)
####
x = random.rand()   #0-1
print(x)
#1-D
x = random.randint(100,size=(5))
print(x)
#2-D
x = random.randint(100,size=(3,5))
print(x)
#Choice
x =random.choice([3,5,7,9],size=(3,5))
print(x)