import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt #자연어 : 사람이 쓰는 언어  ko =한국ㅇ더 pip install konlpy /pip install tweepy==3.10.0
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('./crawling/team_crawling/naver_headline_news.csv')
print(df.head())
print(df.info())

X = df['title']
Y = df['category']

encoder = LabelEncoder()
labeled_Y = encoder.fit_transform(Y)  # 정치 경제 등 숫자로, array타입으로
# print(encoder.classes_) #encoder 의 라벨에 대한 정보

label= encoder.classes_
print(labeled_Y[:5])
print(label)
with open('./models/encoder.pickle', 'wb') as f:
    pickle.dump(encoder, f) #encoder을 f에다가 저장
onehot_Y =  to_categorical(labeled_Y)
print(onehot_Y)


onehot_Y = to_categorical(labeled_Y)
print(onehot_Y)

okt = Okt() # 형태소 분리##
# print(type(X))
# okt_morph_X = okt.morphs(X[10], stem=True)
# print(X[10])
# print(okt_morph_X)


for i in range(len(X)):
    X[i] = okt.morphs(X[i])
# print(X)

stopwords = pd.read_csv('./crawling/stopwords.csv', index_col=0)

for j in range(len(X)):
    words = []
    for i in range(len(X[j])):
        if len(X[j][i]) > 1:
            if X[j][i] not in list(stopwords['stopword']):
                words.append(X[j][i])
    X[j] = ' '.join(words)
print(X)

token = Tokenizer()
token.fit_on_texts(X)
tokened_X = token.texts_to_sequences(X)
print(tokened_X[:5])

with open('./models/news_token.pickle', 'wb') as f:
    pickle.dump(token, f)

wordsize = len(token.word_index) + 1
print(wordsize)
print(token.index_word)

max = 0
for i in range(len(tokened_X)):
    if max < len(tokened_X[i]):
        max = len(tokened_X[i])
print(max)

X_pad = pad_sequences(tokened_X , max)
print(X_pad[:10])

X_train, X_test, Y_train, Y_test = train_test_split(X_pad, onehot_Y, test_size=0.1)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

xy = X_train, X_test, Y_train, Y_test
np.save('./crawling/news_data_max_{}_wordsize_{}'.format(max, wordsize), xy)

# models 폴더에news_category_classification_03_learning.py-