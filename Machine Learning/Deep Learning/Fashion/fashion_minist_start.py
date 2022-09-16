import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras import activations, regularizers
from keras.layers import Dense, Input, Concatenate, Dropout
from keras.models import Model, Sequential
import numpy as np
tf.executing_eagerly()


X_train =  np.load('train_images.npy', allow_pickle=True)
y_train =  np.load('train_labels.npy', allow_pickle=True)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# show image
data_idx = 1
plt.imshow(X_train[data_idx,:,:]/255, cmap='binary')
class_number = y_train[data_idx]
class_text = class_names[class_number]
print(f'This is a {class_text}')


# data prep
X_train = X_train/255
X_train = X_train.reshape(-1, 784)
y_train_ohe = np.zeros(10, 680000)

from sklearn.preprocessing import OneHotEncoder

# create a model and train it:

input_layer = Input(shape=(5,))
first_hidden_layer = Dense(7, activation="relu")(input_layer)
first_hidden_layer_d = Dropout(0.5)(first_hidden_layer)
second_hidden_layer = Dense(7, activation="relu")(first_hidden_layer_d)
second_hidden_layer_d = Dropout(0.5)(second_hidden_layer)
output_layer = Dense(4, activation="softmax")(second_hidden_layer_d)

my_model = Sequential(inputs=input_layer, outputs=output_layer)
my_model.compile(optimizer="adam", loss="categorical_crossentropy") # Best optimizer = "adam", Multi-Class Classification loss allways "categorical_crossentropy"

X = np.array([0.2, 0.65, 0.31, 0.5, 0.25]).reshape(1,5)
print(X.shape)
prediction = my_model.predict(X)
print(f'Multi-Class Classification: {prediction}')




# prep validation data
X_val =  np.load('val_images.npy', allow_pickle=True)

# predic validation data
my_prediction = np.array([0,1,2])

# save predictions
my_name = 'Eivind'
np.save(f'{my_name}_predictions.npy', my_prediction)