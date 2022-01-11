import pandas as pd
pd.options.display.max_rows = 20
pd.set_option('display.unicode.east_asian_width', True)
import warnings
warnings.filterwarnings(action='ignore')
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *



X_train, X_test, Y_train, Y_test = np.load('./crawling/news_data_max_25_size_16643.npy', allow_pickle=True)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

'''모델 생성'''
model = Sequential()
model.add(Embedding(16643, 300, input_length=25))
model.add(Conv1D(32, kernel_size=5, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=1))
model.add(LSTM(128, activation='tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(64, activation='tanh', return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(64, activation='tanh'))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(6, activation='softmax'))
print(model.summary())

'''모델 학습'''
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
fit_hist = model.fit(X_train, Y_train, batch_size=100, epochs=8, validation_data=(X_test,Y_test))

'''모델 저장'''
model.save('./models/news_category_classification_model.h5')

print('\n\n=====DONE=====')
print('    code 0     ')
print('==============')