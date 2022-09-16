import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

df = pd.read_csv('kc_house_data.csv')

y_price = np.c_[df['price']]
X_sqft_living = np.c_[df['sqft_living']]

model = LinearRegression()
model.fit(X=X_sqft_living, y=y_price)



print('\nLinear reg test:')
x_new = [[1000], [1500], [700]]
predictions = model.predict(x_new)
print(model.score(X=X_sqft_living, y=y_price))
y_pred = model.predict(X_sqft_living)
print(np.sqrt(mean_squared_error(y_pred, y_price)))
print(mean_absolute_error(y_pred, y_price))

y_mean = np.mean(y_price)*np.ones(y_price.shape)
print(np.sqrt(mean_squared_error(y_mean, y_price)))
print(mean_absolute_error(y_mean, y_price))


def plot_model(model, X, y):
    x_plot_val = np.linspace(0, max(X)*1.1, num=100).reshape(-1, 1)
    y_plot_val = model.predict(x_plot_val)
    plt.plot(X, y, 'x', alpha=0.3)
    plt.plot(x_plot_val, y_plot_val, 'r-')  
    plt.show


plot_model(model, X_sqft_living, y_price)

model_k_neighbors = KNeighborsRegressor(n_neighbors=5)
model_k_neighbors.fit(X=X_sqft_living, y=y_price)

plot_model(model_k_neighbors, X_sqft_living, y_price)

print('\nLinear neighbor reg test:')

x_new_neighbors = [[1000], [1500], [700]]
predictions = model_k_neighbors.predict(x_new_neighbors)
print(model_k_neighbors.score(X=X_sqft_living, y=y_price))

y_neighbor_pred = model_k_neighbors.predict(X_sqft_living)
print(np.sqrt(mean_squared_error(y_neighbor_pred, y_price)))
print(mean_absolute_error(y_neighbor_pred, y_price))

y_mean = np.mean(y_price)*np.ones(y_price.shape)
print(np.sqrt(mean_squared_error(y_mean, y_price)))
print(mean_absolute_error(y_mean, y_price))


