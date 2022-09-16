from keras import activations, regularizers
from keras.layers import Dense, Input, Concatenate, Dropout
from keras.models import Model
import numpy as np


# Oppgave 1:

# Activation Regression:
input_layer = Input(shape=(3,))
first_hidden_layer = Dense(4, activation="relu", kernel_regularizer=regularizers.l2(0.01))(input_layer) # Add relu activation
output_layer = Dense(2)(first_hidden_layer) # Output layer activation = None

my_model = Model(inputs=input_layer, outputs=output_layer)
my_model.compile(optimizer="adam", loss="mse") # Best optimizer = "adam", Regression loss allways "mse"

X = np.array([0.2, 0.65, 0.31]).reshape(1,3)
print(X.shape)
prediction = my_model.predict(X)
print(f'Regression: {prediction}')


# Oppgave 2:

# Multi-Class Classification:
input_layer = Input(shape=(5,))
first_hidden_layer = Dense(7, activation="relu")(input_layer)
first_hidden_layer_d = Dropout(0.5)(first_hidden_layer)
second_hidden_layer = Dense(7, activation="relu")(first_hidden_layer_d)
second_hidden_layer_d = Dropout(0.5)(second_hidden_layer)
output_layer = Dense(4, activation="softmax")(second_hidden_layer_d)

my_model = Model(inputs=input_layer, outputs=output_layer)
my_model.compile(optimizer="adam", loss="categorical_crossentropy") # Best optimizer = "adam", Multi-Class Classification loss allways "categorical_crossentropy"


X = np.array([0.2, 0.65, 0.31, 0.5, 0.25]).reshape(1,5)
print(X.shape)
prediction = my_model.predict(X)
print(f'Multi-Class Classification: {prediction}')


# Oppgave 3:

# Multi-Label Classification:
input_layer = Input(shape=(4,))
first_hidden_layer = Dense(5, activation="relu")(input_layer)
second_hidden_layer = Dense(7, activation="relu")(first_hidden_layer)
output_layer = Dense(3, activation="sigmoid")(second_hidden_layer)

my_model = Model(inputs=input_layer, outputs=output_layer)
my_model.compile(optimizer="adam", loss="binary_crossentropy") # Best optimizer = "adam", Multi-Label Classification loss allways "binary_crossentropy"

X = np.array([0.2, 0.65, 0.31, 0.5]).reshape(1,4)
print(X.shape)
prediction = my_model.predict(X)
print(f'Multi-Label Classification: {prediction}')


# Oppgave 4:
network_a = Input(shape=(3,))
network_a_h1 = Dense(4, activation="relu")(network_a)
network_a_h2 = Dense(2, activation="relu")(network_a_h1)

network_b = Input(shape=(3,))
network_b_h1 = Dense(4, activation="relu")(network_b)
network_b_h2_no_act = Dense(2)(network_b_h1)
network_b_h2 = activations.relu(network_b_h2_no_act)

network_a_b = Concatenate(axis=1)([network_a_h2, network_b_h2])
network_a_b_h1 = Dense(5, activation="relu")(network_a_b)
network_a_b_h2 = Dense(7, activation="relu")(network_a_b_h1)
network_a_b_h3 = Dense(3, activation="softmax")(network_a_b_h2)

my_model = Model(inputs=[network_a, network_b], outputs=[network_b_h2_no_act, network_a_b_h3])
my_model.compile(optimizer="adam", loss="categorical_crossentropy")

X1 = np.array([0.2, 0.65, 0.31]).reshape(1,3)
print(X1)
X2 = np.array([0.3, 0.74, 0.4]).reshape(1,3)
# prediction = my_model.predict((X1, X2))
# print(f'Regression -> Multi-Class Classification: {prediction}')

# Oppgave 8

# network_a = Input(shape=(3,))
# network_a_h1 = Dense(4, activation="relu")(network_a)
# network_a_h2 = Dense(2, activation="relu")(network_a_h1)

# network_b = Input(shape=(3,))
# network_b_h1 = Dense(4, activation="relu")(network_b)
# network_b_h2_no_act = Dense(2)(network_b_h1)
# network_b_h2 = activations.relu(network_b_h2_no_act)

# network_a_b = Concatenate(axis=1)([network_a_h2, network_b_h2])
# network_a_b_h1 = Dense(5, activation="relu")(network_a_b)
# network_a_b_h2 = Dense(7, activation="relu")(network_a_b_h1)
# network_a_b_h3 = Dense(3)(network_a_b_h2)

# my_model_final = Model(inputs=[network_a, network_b], outputs=[network_b_h2_no_act, network_a_b_h3])

# X1 = np.array([0.2, 0.65, 0.31]).reshape(1,3)
# X2 = np.array([0.3, 0.74, 0.4]).reshape(1,3)
# prediction = my_model_final.predict((X1, X2))
# print(prediction)


# # Oppgave 8

# network_a = Input(shape=(3,))
# network_a_h1 = Dense(4, activation="relu")(network_a)
# network_a_h2 = Dense(2, activation="relu")(network_a_h1)

# network_b = Input(shape=(3,))
# network_b_h1 = Dense(4, activation="relu")(network_b)
# network_b_h2_no_act = Dense(2)(network_b_h1)
# network_b_h2 = activations.relu(network_b_h2_no_act)

# network_a_b = Concatenate(axis=1)([network_a_h2, network_b_h2])
# network_a_b_h1 = Dense(5, activation="relu")(network_a_b)
# network_a_b_h2 = Dense(7, activation="relu")(network_a_b_h1)
# network_a_b_h3 = Dense(3, activation="softmax")(network_a_b_h2)

# my_model_final = Model(inputs=[network_a, network_b], outputs=[network_b_h2_no_act, network_a_b_h3])

# X1 = np.array([0.2, 0.65, 0.31]).reshape(1,3)
# X2 = np.array([0.3, 0.74, 0.4]).reshape(1,3)
# prediction = my_model_final.predict((X1, X2))
# print(f'Regression and Classification: {prediction}')