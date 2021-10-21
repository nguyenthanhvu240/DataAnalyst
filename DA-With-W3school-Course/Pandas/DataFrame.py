import pandas as pd
#Series : Column
#DataFrame : Table

data = {
    'calories':[200,300,400,500,600],
    'duration':[10,20,30,40,50],
}
df = pd.DataFrame(data,index=['day1','day2','day3','day4','day5'])
print(df)
print(df.loc['day2'])
print(df.loc[['day1','day5']])

###### Load File
f = pd.read_csv('data.csv')
print(f)
print(f.to_string())