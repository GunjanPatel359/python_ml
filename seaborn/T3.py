import seaborn as sns
import matplotlib.pyplot as plt

titanic_df=sns.load_dataset('titanic')
print(titanic_df.head())

# sns.scatterplot(x='age',y='fare',data=titanic_df)
# plt.show()

# sns.scatterplot(x='age',y='fare',data=titanic_df,hue="alive")
# plt.show()

# plt.figure(figsize=(12,6))
# sns.scatterplot(x='age',y='fare',data=titanic_df,hue='alive',style='class')
# plt.title('Titanic Data Analysis')
# plt.show()

# plt.figure(figsize=(12,6))
# sns.scatterplot(x='age',y='fare',data=titanic_df,hue='alive',style='class',palette='inferno')
# plt.title('Titanic Data Analysis')
# plt.show()

# plt.figure(figsize=(12,6))
# sns.scatterplot(x='age',y='fare',data=titanic_df,hue='alive',style='class',palette='gist_rainbow',alpha=0.5)
# plt.title('Titanic Data Analysis')
# plt.show()

# plt.figure(figsize=(12,6))
# sns.scatterplot(x='age',y='fare',data=titanic_df,hue='alive',style='class')
# sns.lineplot(x='age',y='fare',data=titanic_df,color='green')
# plt.title('Titanic Data Analysis')
# plt.show()