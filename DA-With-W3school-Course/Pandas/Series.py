import pandas as pd

a = [3,7,2]
myvar = pd.Series(a)
print(myvar)
print(myvar[1])
###
a = [4,5,6]
myvar = pd.Series(a,index=['x','y','z'])
print(myvar)
###
calories = {
    'day1' : 420,
    'day2' : 380,
    'day3' : 'abc',
}
myvar = pd.Series(calories)
print(myvar)
print(myvar['day2'])
####
col = {
    'day1':420,
    'day2':380,
    'day3' : 'xyz'
}
myvar = pd.Series(col,index=['day1','day2'])
print(myvar)