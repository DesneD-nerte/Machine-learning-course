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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

grid_searcher = GridSearchCV(KNeighborsRegressor(),
                             param_grid={
                                 'n_neighbors': [1, 5, 10, 20],
                                'weights': ['uniform', 'distance'],
                                'p': [1, 2, 3]
                                         },
                             cv=5)

grid_searcher.fit(X_train, y_train)
best_predictions = grid_searcher.predict(X_test)
print("Среднеквадратичное отклонение:", mean_squared_error(y_test, best_predictions))
print("Лучшие параметры:", grid_searcher.best_params_)


