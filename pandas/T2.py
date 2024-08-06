import pandas as pd

df=pd.DataFrame()
print(df)

lst=[1,2,3,4,5]
df=pd.DataFrame(lst)
print(df)

lst=[[1,2,3,4,5],[11,12,13,14,15]]
df=pd.DataFrame(lst)
print(df)

a=[{'a':5,'b':7,'c':9,'d':2},{'a':4,'b':8,'c':19,'d':12}]
df=pd.DataFrame(a)
print(df)

b={'RollNo.':pd.Series([1,2,3,4,5]),
   'Maths':pd.Series([67,89,23,90,56]),
   'Physics':pd.Series([12,98,44,90,78])}

df=pd.DataFrame(b)
print(df)

df=pd.read_csv('./pandas/Datasets/Salary_Data.csv')
print(df)
print(type(df))