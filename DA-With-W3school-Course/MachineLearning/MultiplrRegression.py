import pandas
df = pandas.read_csv('cars.csv')

# It is common to name the list of independent values with a upper case X, and the list of dependent values with a lower case y.
X = df[['Weight', 'Volume']]
y = df['CO2']

from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X,y)

##predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictCO2 = regr.predict([[2300,1300]])
print(predictCO2)

### Coefficient
df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)
"""The result array represents the coefficient values of weight and volume.

Weight: 0.00755095
Volume: 0.00780526

These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.
And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.
I think that is a fair guess, but let test it!
We have already predicted that if a car with a 1300cm3 engine weighs 2300kg, the CO2 emission will be approximately 107g.
What if we increase the weight with 1000kg?
"""
