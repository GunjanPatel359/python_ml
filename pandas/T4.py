import pandas as pd

df=pd.read_csv('./pandas/Datasets/sample.csv')
print(df.head())
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())
print(df.shape)
df2=df.dropna()
print(df2)
print(df2.shape)
df3=df.dropna(axis=1)
print(df3)
print(df3.shape)
print(df.dropna(how='any')) # if any row value is null then remove that row
print(df.dropna(how='all')) # if all row values is null then remove that row
# print(df.dropna(inplace=True)) #do not use this
print(df.shape)