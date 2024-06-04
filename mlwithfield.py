import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError
import csv
import elliptic_operations as e_i
import makedata as md


with open('datax') as f:
    reader = csv.reader(f)
    x = list(reader)
with open('datay') as f:
    reader = csv.reader(f)
    y = list(reader)

x = np.array(x, dtype=int)
y = np.array(y, dtype=int)

print(x.shape)
print(y.shape)

# define the keras model
model = Sequential()
model.add(Dense(12, input_shape=(7,), activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dense(400, activation='relu'))
model.add(Dense(800, activation='relu'))
model.add(Dense(11, activation='sigmoid'))

# compile the keras model
model.compile(loss=MeanSquaredError, optimizer=Adam(learning_rate=1e-5), metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(x, y, epochs=10, batch_size=10)
# evaluate the keras model

_, accuracy = model.evaluate(x, y)

G = e_i.point(3, 6, 7919, 2, 3)
x, y = md.calcpoint(G, 500, 1008, 1008)

'''
# figure out what shape data needs to be
x = np.swapaxes(np.array(x), 0, 1)
y = np.swapaxes(np.array(y), 0, 1)
'''

x = np.array(x)
y = np.array(y)

_, accuracy = model.evaluate(x, y)
