import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.metrics.pairwise import euclidean_distances
# from sklearn.model_selection import KFold
# from sklearn.cluster import KMeans
from datetime import datetime

df = pd.read_csv('sphist.csv')

df["Date"] = pd.to_datetime(df["Date"])
df.sort_values(by='Date', ascending=True, inplace=True)
df.reset_index(drop=True, inplace=True)

#Add features that could be helpful for machine learning
df['5 Days Open'] = df['Open'].rolling(center=False, window=5).mean()
df['5 Days High'] = df['High'].rolling(center=False, window=5).mean()
df['5 Days Low'] = df['Low'].rolling(center=False, window=5).mean()
df['5 Days Volume'] = df['Volume'].rolling(center=False, window=5).mean()

df['Year'] = df['Date'].apply(lambda x: x.year)

#Adding Day of week column and set it to categorical
df['DOW'] = df['Date'].apply(lambda x: x.weekday())
dow_df = pd.get_dummies(df['DOW'])
df = pd.concat([df, dow_df], axis=1)
df = df.drop(['DOW'], axis=1)

#Shift the columns by one
df['5 Days Open'] = df['5 Days Open'].shift(1)
df['5 Days High'] = df['5 Days High'].shift(1)
df['5 Days Low'] = df['5 Days Low'].shift(1)
df['5 Days Volume'] = df['5 Days Volume'].shift(1)

df = df[df['Date'] >= datetime(year=1951, month=1, day=3)]
df.dropna(axis=0)

# Create train and test dataframes
train = df[df["Date"] < datetime(year=2013, month=1, day=1)]
test = df[df["Date"] >= datetime(year=2013, month=1, day=1)]

features = ['5 Days Open', '5 Days Volume', '5 Days High', '5 Days Low', 'Year', 0, 1, 2, 3, 4]

lr = LinearRegression()
lr.fit(train[features], train['Close'])
predictions = lr.predict(test[features])

mae = mean_absolute_error(test['Close'] ,predictions)

print(df.tail(1))
print(mae)