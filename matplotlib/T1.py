import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('dark_background')

# rollno=[1,2,3,4,5,6,7,8,9,10]
# marks=[10,20,30,40,50,60,70,80,90,100]

# plt.scatter(rollno,marks)
# plt.show()

# plt.scatter(rollno,marks,color='blue')
# plt.show()

# plt.scatter(rollno,marks,color='blue',marker='*')
# plt.show()

# plt.figure(figsize=(12,8))
# plt.scatter(rollno,marks,color='blue',marker='*')
# plt.show()

# plt.figure(figsize=(8,8))
# plt.plot(rollno,marks,'bo',markersize=20)
# plt.show()

temperature_pune=[25,34,21,45,28,6,43,18,7,2]
humidity_pune=[28,25,29,20,26,50,19,29,52,55]

temperature_bangalore=[34,35,36,37,28,27,26,25,31,20]
humidity_bangalore=[40,38,36,35,42,44,41,40,34,45]

# plt.figure(figsize=(8,8))
# plt.plot(temperature_pune,humidity_pune,'ro',markersize=15)
# plt.show()

# plt.figure(figsize=(8,8))
# plt.xticks(np.arange(0,60,5))
# plt.yticks(np.arange(10,60,5))
# plt.plot(temperature_pune,humidity_pune,'ro',markersize=15)
# plt.xlabel('Temperature')
# plt.xlabel('Humidity')
# plt.show()

# plt.figure(figsize=(8,8))
# plt.xticks(np.arange(0,60,5))
# plt.yticks(np.arange(10,60,5))
# plt.plot(temperature_pune,humidity_pune,'ro',markersize=15)
# plt.plot(temperature_bangalore,humidity_bangalore,'bo',markersize=15)
# plt.xlabel('Temperature')
# plt.xlabel('Humidity')
# plt.show()

df=pd.read_csv('./matplotlib/IRIS.csv')
print(df.head())

# plt.scatter(df['sepal_length'],df['petal_length'])
# plt.show()

# plt.scatter(df['sepal_width'],df['petal_width'],'go')
# plt.show()

plt.figure(figsize=(8,8))
plt.xticks(np.arange(1,10,0.5))
plt.yticks(np.arange(1,10,0.5))
plt.plot(df['sepal_length'],df['petal_length'],'ro',alpha=0.5,markersize=8)
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()