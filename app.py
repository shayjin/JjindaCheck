import tensorflow as tf
import pandas as pd
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data = pd.read_csv('data.csv')

#data.isnull().sum()
#data.dropna()

y = data['admit'].values

x = []

for i, rows in data.iterrows():
    x.append([rows['title'], rows['text']])

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(np.array(x), np.array(y), epochs=50)

prediction = model.predict([[1,1]])

print(prediction)