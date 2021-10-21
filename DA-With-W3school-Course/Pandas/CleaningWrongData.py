from numpy.core.numeric import NaN
import pandas as pd
df = pd.read_csv('dirtydata.csv')
#df.loc[7,'Duration'] = 1122    Replace

#for d in df.index:  
#    if df.loc[d,'Duration'] > 120:
#        df.loc[d,'Duration'] = 1212
for c in df.index:
    if df.loc[c,'Calories'] == 280.0:
        df.drop(c,inplace=True)
print(df.to_string())