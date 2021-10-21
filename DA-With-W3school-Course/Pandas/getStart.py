import pandas as pd

mydataset = {
    'car' : ['BMW','Volve','Ford'],
    'passing' : [3,7,2]
}
myvar = pd.DataFrame(mydataset)

print(myvar)