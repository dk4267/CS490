import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#open file, take out null data
data = pd.read_csv('train.csv')
newData = data.select_dtypes(include=[np.number]).interpolate().dropna()

#filter outliers with a high z score
z = np.abs(stats.zscore(newData))
newData = newData[(z < 2).all(axis=1)]

#create scatter plot with data minus outliers
plt.scatter(newData['GarageArea'], newData['SalePrice'], alpha=.75,
            color='b') #alpha helps to show overlapping data
plt.xlabel('Garage Area')
plt.ylabel('Sale Price')
plt.title('Linear Regression Model')
plt.show()

