import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# flight_df=sns.load_dataset('flights')
# print(flight_df.head())

# flight_df=flight_df.pivot(columns='year',index='month',values='passengers')
# print(flight_df.head())

# plt.figure(figsize=(12,6))
# sns.heatmap(flight_df)
# plt.show()

# plt.figure(figsize=(14,8))
# sns.heatmap(flight_df,annot=True,fmt='d')
# plt.show()

# plt.figure(figsize=(14,8))
# sns.heatmap(flight_df,annot=True,fmt='d',linecolor='w',linewidths='5')
# plt.show()

# plt.figure(figsize=(14,8))
# sns.heatmap(flight_df,annot=True,fmt='d',linecolor='k',linewidths='5',cmap='Blues')
# plt.show()

# plt.figure(figsize=(14,8))
# sns.heatmap(flight_df,cbar=False)
# plt.show()

# grid_kws={'height_ratios':(.4,.05),'hspace':.4}
# f,(ax,cbar_ax)=plt.subplots(2,gridspec_kw=grid_kws)
# sns.heatmap(flight_df,cbar_kws={'orientation':"horizontal"},ax=ax,cbar_ax=cbar_ax)
# plt.show()

# titanic_df=sns.load_dataset('titanic')
# print(titanic_df.head())
# print(titanic_df.corr())
# plt.figure(figsize=(12,8))
# sns.heatmap(titanic_df.corr())
# plt.show()