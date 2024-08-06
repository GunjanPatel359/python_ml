import pandas as pd

# df1=pd.DataFrame({'Roll No.':[1,2,3,4,5],'Maths':[45,78,45,90,66],'Physics':[33,67,12,90,44]})
# df2=pd.DataFrame({'Roll No.':[6,7,8,9,10],'Maths':[78,73,45,90,69],'Physics':[23,67,88,0,98]})

# print(df1)
# print(df2)

# print(df1._append(df2))
# print(df2._append(df1))
# print(df1._append(df2,ignore_index=True))
# print(df1._append(df2,ignore_index=True,sort=True))

# df1=pd.DataFrame({'Roll No.':[1,2,3,4,5],'Chemistry':[45,78,45,90,66],'Physics':[33,67,12,90,44]})
# df2=pd.DataFrame({'Roll No.':[6,7,8,9,10],'Maths':[78,73,45,90,69],'Physics':[23,67,88,0,98]})
# print(df1)
# print(df2)
# print(df1._append(df2,ignore_index=True))


df1=pd.DataFrame({'Roll No.':[1,2,3,4,5],'Maths':[45,78,45,90,66],'Physics':[33,67,12,90,44],'Chemistry':[56,89,33,12,89]})
df2=pd.DataFrame({'Roll No.':[6,7,8,9,10],'Maths':[78,73,45,90,69],'Physics':[23,67,88,0,98]})
print(df1)
print(df2)
print(df1._append(df2,ignore_index=True))