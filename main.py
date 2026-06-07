import pandas as pd
import numpy as np

df = pd.read_csv('all_stocks_5yr.csv')

#SMA
df["SMA20"] = df.groupby("Name")["close"].transform(lambda x: x.rolling(window=20).mean())
df["SMA5"] = df.groupby("Name")["close"].transform(lambda x: x.rolling(window=5).mean())

#Bollinger Bands
rolling_std = df.groupby("Name")["close"].transform(lambda x: x.rolling(window=20).std())
df["BBUpper"] = df["SMA20"] + 2 * rolling_std
df["BBLower"] = df["SMA20"] - 2 * rolling_std

df.dropna(inplace=True)

#SMA signals
SMAconditions = [df["SMA5"] > df["SMA20"], df["SMA5"] < df["SMA20"]]
SMAchoices = [1, -1]
df["SMAsignal"] = np.select(SMAconditions, SMAchoices, default=0)

#Bands signals

Bconditions = [df["close"] < df["BBLower"], df["close"] > df["BBUpper"]]
Bchoices = [1, -1]
df["Bsignal"] = np.select(Bconditions, Bchoices, default=0)

df["stock daily returns"] = df.groupby("Name")["close"].pct_change()
df["Bbands daily returns"] = df["stock daily returns"] * df.groupby("Name")["Bsignal"].shift(1)
df["SMA daily returns"] = df["stock daily returns"] * df.groupby("Name")["SMAsignal"].shift(1)

df = df.fillna(0)

#buy and hold
df["Buy and Hold"] = df.groupby("Name")["stock daily returns"].transform(lambda x: (1 + x).cumprod())
df["Bollinger Bands returns"] = df.groupby("Name")["Bbands daily returns"].transform(lambda x: (1 + x).cumprod())
df["SMA returns"] = df.groupby("Name")["SMA daily returns"].transform(lambda x: (1 + x).cumprod())

columns_to_save = ['Name', 'Buy and Hold', 'SMA returns', 'Bollinger Bands returns']
df[columns_to_save].to_csv("backtest_results.csv")