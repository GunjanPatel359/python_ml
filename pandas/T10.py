import pandas as pd
df=pd.read_csv('./pandas/Datasets/sample2.csv')
print(df.head())

print(pd.pivot_table(df,index='Branch',aggfunc='sum'))
print(pd.pivot_table(df,index='Branch',aggfunc='count'))
print(pd.pivot_table(df,index='Branch',aggfunc='max'))