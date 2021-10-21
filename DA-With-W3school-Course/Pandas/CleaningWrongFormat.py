import pandas as pd

df = pd.read_csv('dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date']) #replace
df.dropna(subset=['Date'],inplace=True) #drop na
print(df.to_string())