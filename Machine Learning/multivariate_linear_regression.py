from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import pandas as pd

df = pd.read_csv('kc_house_data.csv')

y_price = np.c_[df['price']]
X_input_columns = np.c_[df[['sqft_living', 'sqft_lot', 'bathrooms', 'bedrooms']]]

model = LinearRegression()
model.fit(X=X_input_columns, y=y_price)

x_new = [[1200, 15000, 2, 1], [950, 7500, 1, 4], [880, 20000, 3, 2]]

predictions = model.predict(x_new)
print(model.score(X=X_input_columns, y=y_price))
y_pred = model.predict(X_input_columns)
print(np.sqrt(mean_squared_error(y_pred, y_price)))
print(mean_absolute_error(y_pred, y_price))


model_kn = KNeighborsRegressor(n_neighbors=5)
model_kn.fit(X=X_input_columns, y=y_price)

predictions_kn = model_kn.predict(x_new)
print(model_kn.score(X=X_input_columns, y=y_price))
y_pred_kn = model_kn.predict(X_input_columns)
print(np.sqrt(mean_squared_error(y_pred_kn, y_price)))
print(mean_absolute_error(y_pred_kn, y_price))
