import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

roll_no=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
marks=[23,45,67,89,56,34,21,45,67,32,67,76,33,21,45]
sample_df=pd.DataFrame({'Roll No':roll_no,'Marks':marks})
print(sample_df.head())

# sns.lineplot(x='Roll No',y='Marks',data=sample_df)
# plt.title('Student Marks')
# plt.show()

# seaborn_df=sns.load_dataset('planets')
# print(seaborn_df.head())

# seaborn_df=sns.load_dataset('titanic')
# print(seaborn_df.head())

# df=pd.read_csv('./seaborn/hr_data.csv')
# print(df.head())

# sns.lineplot(x='number_project',y='average_montly_hours',data=df)
# plt.show()

# sns.lineplot(x='promotion_last_5years',y='left',data=df)
# plt.show()

# plt.figure(figsize=(12,6))
# sns.lineplot(x='department',y='left',data=df)
# plt.show()

# sns.lineplot(x='number_project',y='average_montly_hours',data=df,hue='left')
# plt.show()

# sns.lineplot(x='number_project',y='average_montly_hours',data=df,hue='department')
# plt.show()

# plt.figure(figsize=(12,6))
# sns.lineplot(x='number_project',y='average_montly_hours',data=df,hue='left',style='department')
# plt.show()

# plt.figure(figsize=(12,6))
# sns.lineplot(x='number_project',y='average_montly_hours',data=df,hue='left',style='department',legend=False)
# plt.show()

# plt.figure(figsize=(12,6))
# sns.lineplot(x='number_project',y='average_montly_hours',data=df,hue='left',style='department',legend=False,palette='flare')
# plt.show()