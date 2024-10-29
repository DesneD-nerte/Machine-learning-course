from matplotlib import pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import numpy as np


data = fetch_california_housing()

X, y = data.data, data.target

# Пример графика
print("Размер матрицы объектов: ", X.shape)
print("Рaзмер вектора y: ", y.shape)
plt.scatter(X[:,0], y)
plt.xlabel('Crime rate')
plt.ylabel('Price')
plt.show()
# Пример графика

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knn = KNeighborsRegressor(n_neighbors=5, weights='uniform', p=2)
knn.fit(X_train, y_train)
predicted_array = knn.predict(X_test)

print("Предсказание базовой модели:", predicted_array)
print("Среднеквадратичное отклонение:", mean_squared_error(y_test, predicted_array))


