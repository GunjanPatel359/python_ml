import seaborn as sns
import matplotlib.pyplot as plt

titanic_df=sns.load_dataset('titanic')
print(titanic_df.head())

# sns.barplot(x='class',y='fare',data=titanic_df)
# plt.show()

# sns.barplot(x='class',y='fare',data=titanic_df,hue='sex')
# plt.show()


# sns.barplot(x='class',y='fare',data=titanic_df,hue='sex',palette='inferno')
# plt.show()

# sns.barplot(x='class',y='fare',data=titanic_df,hue='sex',palette='inferno',estimator=np.max)
# plt.show()

# sns.barplot(x='class',y='fare',data=titanic_df,hue='sex',palette='inferno',ci=100,errcolor='red',errwidth=10)
# plt.show()

# sns.barplot(x='class',y='fare',data=titanic_df,hue='sex',palette='inferno',saturation=0.3)
# plt.show()