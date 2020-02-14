import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

data = pd.read_csv('glass.csv')
X_train = data.drop(['Type'], axis=1)
Y_train = data['Type']

X_train, X_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=0.4, random_state=0)

naiveBayes = GaussianNB()
prediction = naiveBayes.fit(X_train, y_train).predict(X_test)

print(classification_report(y_test, prediction))
