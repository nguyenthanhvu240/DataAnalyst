import pandas as pd

df = pd.read_csv('dirtydata.csv')
print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df.to_string())