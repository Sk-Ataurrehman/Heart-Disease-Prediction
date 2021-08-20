import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
ds = pd.read_csv('Dataset.csv')

y=ds.iloc[:,-1].values
x=ds.iloc[:,:-1].values

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x, y)
y_pred = knn.predict(x)
print("Accuracy: ")
print(metrics.accuracy_score(y, y_pred)*100,"%")