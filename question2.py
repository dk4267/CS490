import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

#Read file, handle null values
data = pd.read_csv('winequality-red.csv')
dataNotNull = data.select_dtypes(include=[np.number]).interpolate().dropna()

#Find top 3 correlated features to target
numeric_features = dataNotNull.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print (corr['quality'].sort_values(ascending=False)[1:4], '\n')

#Set up training and testing
y = dataNotNull['quality']
x = dataNotNull.drop(['quality'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(
                                    x, y, random_state=42, test_size=.33)
#Set up linear regression model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

#RMSE test
predictions = model.predict(X_test)
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

#R squared test
print ("R^2 is: \n", model.score(X_test, y_test))

