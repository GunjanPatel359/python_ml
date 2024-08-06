import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('./seaborn/hr_data.csv')
print(df.head())

# sns.displot(df['time_spend_company'])
# plt.show()

# sns.displot(df['left'])
# plt.show()

# sns.displot(df['average_montly_hours'])
# plt.show()

# print(df.describe())

# bins=[2,3,4,5,6,7,8,9,10]
# sns.displot(df['time_spend_company'],bins=bins)
# plt.xticks(bins)
# plt.show()

# bins=[2,3,4,5,6,7,8,9,10]
# sns.displot(df['time_spend_company'],bins=bins,kde=True)
# plt.show()

# bins=[2,3,4,5,6,7,8,9,10]
# sns.displot(df['time_spend_company'],bins=bins,kde=True,hist=False)
# plt.show()

# bins=[2,3,4,5,6,7,8,9,10]
# sns.displot(df['time_spend_company'],bins=bins,kde=True,rug=True)
# plt.xticks(bins)
# plt.show()

# bins=[2,3,4,5,6,7,8,9,10]
# sns.displot(df['time_spend_company'],bins=bins,kde=True,rug=True, rug_kws={'color':'red','edgecolor':'blue','linewidth':3,'alpha':0.5})
# plt.xticks(bins)
# plt.show()

bins=[2,3,4,5,6,7,8,9,10]
sns.displot(df['time_spend_company'],bins=bins,kde=True,rug=True,color='orange')
plt.xticks(bins)
plt.show()
