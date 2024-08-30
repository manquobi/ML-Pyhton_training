print('hello')
import pandas 
from sklearn import linear_model 
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

df = pandas.read_csv("data.csv") 
X = df[['Weight', 'Volume']]
y = df['CO2'] 
regr = linear_model.LinearRegression()
regr.fit(X, y) 
predictedCO2 = regr.predict([[2300, 1300]]) 
print(predictedCO2)
df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2) 

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX) 

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2) 
