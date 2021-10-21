"""
The standardization method uses this formula:
z = (x - u) / s
Where z is the new value, x is the original value, u is the mean and s is the standard deviation.
If you take the weight column from the data set above, the first value is 790, and the scaled value will be:
(790 - 1292.23) / 238.74 = -2.1
If you take the volume column from the data set above, the first value is 1.0, and the scaled value will be:
(1.0 - 1.61) / 0.38 = -1.59
"""
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
df = pandas.read_csv("cars.csv")
X = df[['Weight', 'Volume']]
scaledX = scale.fit_transform(X)
print(scaledX)

#Predict CO2 Values
print("+++++++++++++++++++++++++")
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(scaledX,y)
scaled = scale.transform([[2300,1.3]])
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)