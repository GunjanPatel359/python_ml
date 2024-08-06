import pandas as pd

df=pd.read_csv('./pandas/Datasets/sample.csv')
print(df.head())

print(df.replace(to_replace=26,value=30))
print(df.replace(34,10000))
print(df.replace(to_replace=[50,51,52,53,54,55,56,57,58,59],value='A'))
print(df.replace(to_replace=[50,51,52,53],value=['A','B','C','D']))
# print(df['Physics'].replace(to_replace=[50,51,52,53], value= ['A', 'B', 'C', 'D'], inplace = True)) # do not use this
print(df.replace('[A-Za-z]',0,regex=True))
print(df.replace(to_replace=15,method='ffill'))
print(df.replace(to_replace=15,method='bfill'))