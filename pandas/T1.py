import pandas as pd

lst=[1,2,3,4,5,6]
print(lst)

series=pd.Series(lst)
print(series)
print(type(series))

empty=pd.Series([])
print(empty)

a=pd.Series(['p','q','r','s','t'],index=[10,11,12,13,14])
print(a)

b=pd.Series(['p','q','r','s','t'],index=[10,11,12,13,14],name='alphabets')
print(b)

scalar_series=pd.Series(0.5)
print(scalar_series)

scalar_series=pd.Series(0.5,index=[1,2,3])
print(scalar_series)

dict_series=pd.Series({'p':1,'q':2,'r':3,'s':4,'t':5})
print(dict_series)
print(dict_series[0])
print(dict_series[0:3])
print(max(dict_series))

dict_series=pd.Series({'p':[1,5,6],'q':[2,6,7],'r':[3,9,0],'s':[4,4,5],'t':[5,1,2]})
print(dict_series)

