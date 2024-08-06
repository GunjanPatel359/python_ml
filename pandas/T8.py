import pandas as pd
df=pd.read_csv('./pandas/Datasets/sample2.csv')
print(df.head())

branch_group=df.groupby(by='Branch')
print(branch_group)
print(branch_group.groups)

branch_group=df.groupby(by=['Branch','Section'])
print(branch_group.groups)

for group,data_frame in branch_group:
    print(group)
    print(data_frame)

df1=pd.DataFrame({'Roll No.':[1,2,3,4,5],'Physics':[34,67,34,89,12]})
print(df1)

df2=pd.DataFrame({'Roll No.':[1,2,3,4,5],'Chemistry':[78,33,39,81,90]})
print(df2)

print(pd.merge(df1,df2,on='Roll No.'))
print(pd.merge(df2,df1,on='Roll No.'))
print(pd.merge(df1,df2))

df3=pd.DataFrame({'Roll No.':[1,2,3,6,7],'Physics':[34,67,34,89,12]})
df4=pd.DataFrame({'Roll No.':[1,2,3,8,9],'Chemistry':[34,67,34,89,12]})
print(pd.merge(df3,df4))

print(pd.merge(df3,df4,how='left'))
print(pd.merge(df3,df4,how='right'))
print(pd.merge(df3,df4,how='outer'))