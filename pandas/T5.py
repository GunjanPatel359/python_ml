import pandas as pd

df=pd.read_csv('./pandas/Datasets/sample.csv')
print(df.head())
print(df.isnull().sum())
print(df.fillna(0))
print(df.fillna(2))
print(df.fillna({'Physics':'none','Chemistry':0,'Maths':30}))
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill',axis=1))
print(df.fillna(method='bfill'))
print(df['Physics'].fillna(value=df['Physics'].mean()))
# print(df.fillna(method='bfill',inplace=True)) #do not use this 
