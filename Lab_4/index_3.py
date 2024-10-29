from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsRegressor
from matplotlib import pyplot as plt
import numpy as np

data = fetch_california_housing()

X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

metrics = []
for n in range(1, 40, 2):
  knn = KNeighborsRegressor(n_neighbors=n)
  scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
  metrics.append(np.mean(scores))

plt.plot(range(1, 40, 2), metrics)
plt.ylabel('Отрицательная среднеквадратичная ошибка')
plt.xlabel('Количество соседей')

plt.show()
