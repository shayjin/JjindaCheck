from io import StringIO
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from collections import Counter

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data = pd.read_csv('data.csv')

#data.isnull().sum()
#data.dropna()

def counter_word(text_col):
    count = Counter()
    for text in text_col.values:
        for word in text.split():
            count[word] += 1
    return count

def decode(sequence):
    return " ".join([reverse_word_index.get(idx, "?") for idx in sequence])


train_size = int(data.shape[0] * 0.8)
train_data = data[:train_size]

tokenizer = Tokenizer(num_words=len(counter_word(data['말']))+100)


tokenizer.fit_on_texts(data['말'])
word_index = tokenizer.word_index




train_sequences = tokenizer.texts_to_sequences(data['말'])
padded = pad_sequences(train_sequences, maxlen=100, padding="post", truncating="post")


reverse_word_index = dict([(idx, word) for (word, idx) in word_index.items()])

decoded_text = decode(train_sequences[0])


y = data['분류'].values

x = []




model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(padded, np.array(y), epochs=1)

from io import StringIO

input = StringIO("""말;
                    우리집에 닭없음ㅋㅋ j dd 우리집에 닭없음ㅋㅋ 나는 찐따입니다. 우리집에 닭없음ㅋㅋ
                    """)
input = pd.read_csv(input, sep=";")


sequences = tokenizer.texts_to_sequences(input['말'])

modified = []


print(sequences)

print(decode(sequences[0]))


val_padded = pad_sequences(sequences, maxlen=100, padding="post", truncating="post")

print("HERE")
print(input)
print(sequences)
print(val_padded)
prediction = model.predict(val_padded)

print("찐따일 확률은 " + str(float(prediction[0][0]) * 100) + "% 입니다")