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

y = []

def counter_word(text_col):
    count = Counter()
    for i in range(len(text_col)):
        text = text_col[i]
        for word in text.split():
            count[word] += 1
            y.append(data['분류'][i])
    return count

def decode(sequence):
    return " ".join([reverse_word_index.get(idx, "?") for idx in sequence])


train_data = data[:data.shape[0]]

num = len(counter_word(data['말']))

tokenizer = Tokenizer(oov_token='이많은데이터에서인식하지못하는단어가나오면찐따언어로인식함')


tokenizer.fit_on_texts(data['말'])
word_index = tokenizer.word_index




train_sequences = tokenizer.texts_to_sequences(data['말'])

n = []
trash = []

for sequence in train_sequences:
    for word in sequence:
        if word not in trash:
            a = []
            a.append(word)
            n.append(a)
            trash.append(word)

print(n)



reverse_word_index = dict([(idx, word) for (word, idx) in word_index.items()])

decoded_text = decode(train_sequences[0])


x = []




model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(np.array(n), np.array(y), epochs=100)

from io import StringIO

input = StringIO("""말;
                     닥쳐! 일단 우리집에 닭없음ㅋㅋ 유백이 갱갱!
                    """)
input = pd.read_csv(input, sep=";")
print(word_index)

sequences = tokenizer.texts_to_sequences(input['말'])

n = []

for sequence in sequences:
    for word in sequence:
        a = []
        a.append(word)
        n.append(a)

print(n)

modified = []



print(decode(sequences[0]))




print("HERE")
print(n)
prediction = model.predict(n)

print(prediction)
print("찐따일 확률은 " + str(float(1 - np.mean(prediction)) * 100) + "% 입니다")