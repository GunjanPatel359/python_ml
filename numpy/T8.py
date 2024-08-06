import numpy as np

s1='Gunjan is my name'
s2='I am an Indian'

print(np.char.add(s1,s2))
print(np.char.upper(s1))
print(np.char.lower(s1))
print(np.char.split(s1))

s3='Gunjan is my\nname'
print(np.char.splitlines(s3))
print(np.char.replace(s1,'name','sirname'))

print(np.char.center('good bye',50,'*'))