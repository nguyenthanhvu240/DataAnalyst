import pandas as pd

'''
df = pd.read_csv('dirtydata.csv')
print(df.to_string())
'''
###Not remove the original
'''
df = pd.read_csv('dirtydata.csv')
new_df = df.dropna()
print(new_df.to_string())
'''

####Remove the original
'''
df = pd.read_csv('dirtydata.csv')
df.dropna(inplace=True)
print(df.to_string())
'''

###Replace empty values
df = pd.read_csv('dirtydata.csv')
df.fillna('Replace',inplace=True)
print(df.to_string())

###Replace just a specify column
df = pd.read_csv('dirtydata.csv')
df['Calories'].fillna('Replace',inplace=True)
print(df.to_string())

#Replace
'''
    @param Mean :Mean = the average value (the sum of all values divided by number of values).
    @param Median = the value in the middle, after you have sorted all values ascending.
    @param Mode = the value that appears most frequently.
'''
df = pd.read_csv('dirtydata.csv')
x = df["Calories"].mean()
#x = df["Calories"].median()
#x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df.to_string())
