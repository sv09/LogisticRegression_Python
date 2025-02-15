import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from logisticRegression import LogisticRegression

bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

clf = LogisticRegression(lr=0.1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

def accuracy(y_pred, y):
    return np.sum(y_pred==y)/len(y)

acc = accuracy(y_pred, y_test)
print("Model accuracy = ", acc*100)