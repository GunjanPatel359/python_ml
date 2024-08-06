import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('dark_background')

subjects=['Maths','English','Science','Social Studies','Computer']
marks=[89,90,45,78,99]

# plt.bar(subjects,marks)
# plt.show()

colors=['red','blue','green','orange','purple']
# plt.bar(subjects,marks,color=colors)
# plt.show()
 
# plt.bar(subjects,marks,color=colors,width=0.6)
# plt.show()

# plt.bar(subjects,marks,color=colors,edgecolor='white')
# plt.show()

# plt.bar(subjects,marks,color=colors,edgecolor='white',linewidth=4)
# plt.show()

# plt.bar(subjects,marks,color=colors,edgecolor='white',linewidth=4,linestyle='--')
# plt.show()

# plt.barh(subjects,marks,color=colors)
# plt.show()

subjects=['Maths','English','Science','Social Studies','Computer']
marks1=[89,90,45,78,99]
marks2=[78,56,34,90,12]

# plt.figure(figsize=(8,8))
# plt.bar(subjects,marks1)
# plt.bar(subjects,marks2)
# plt.xlabel('Subjects')
# plt.ylabel('Marks')
# plt.show()

# subjects_len=np.arange(len(subjects))
# width=0.4

# plt.figure(figsize=(8,8))
# plt.bar(subjects_len,marks1,width=width)
# plt.bar(subjects_len+width,marks2,width=width)
# plt.xlabel('Subjects')
# plt.ylabel('Marks')
# plt.show()

# plt.figure(figsize=(8,8))
# plt.bar(subjects_len,marks1,width=width,color=colors)
# plt.bar(subjects_len+width,marks2,width=width,color=colors,alpha=0.5)
# plt.xlabel('Subjects')
# plt.ylabel('Marks')
# plt.show()

# df=pd.read_csv('./matplotlib/SUPERMARKET.csv')
# print(df.head())

# payment_df=pd.DataFrame(df['Payment'].value_counts())
# print(payment_df)

# colors=['red','blue','green']
# plt.bar(payment_df.index,payment_df['count'],color=colors)
# plt.show()