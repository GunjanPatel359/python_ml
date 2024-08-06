import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('dark_background')

classes=['Physics','Chemistry','Maths','Science','SST']
marks=[89,45,78,23,90]

# plt.pie(marks,labels=classes)
# plt.show()

colors=['red','blue','green','#9803fc','#03c2fc']
# plt.pie(marks,labels=classes,colors=colors)
# plt.show()

# plt.pie(marks,labels=classes,colors=colors,autopct='%0.2f%%')
# plt.show()

# explode_values=[0.1,0,0,0,0]
# plt.pie(marks,labels=classes,colors=colors,autopct='%0.2f%%',explode=explode_values)
# plt.show()

# explode_values=[0.1,0.3,0.4,0,0.2]
# plt.pie(marks,labels=classes,colors=colors,autopct='%0.2f%%',explode=explode_values,shadow=True)
# plt.show()

# explode_values=[0.1,0.2,0,0,0]
# plt.pie(marks,labels=classes,colors=colors,autopct='%0.2f%%',explode=explode_values,radius=1.6)
# plt.show()

# explode_values=[0.1,0.3,0,0,0]
# textprops={'fontsize':14,'color':'k'}
# plt.pie(marks,labels=classes,colors=colors,autopct='%0.2f%%',explode=explode_values,radius=1.6,textprops=textprops)
# plt.show()

# explode_values=[0.1,0.4,0,0.2,0]
# textprops={'fontsize':14,'color':'k'}
# wedgeprops={'linewidth':3,'linestyle':'--','edgecolor':'white'}
# plt.pie(marks,labels=classes,colors=colors,autopct='%0.2f%%',explode=explode_values,radius=1.6,textprops=textprops,wedgeprops=wedgeprops)
# plt.show()

# plt.figure(figsize=(6,6))
# explode_values=[0.1,0.4,0,0.2,0]
# textprops={'fontsize':14,'color':'k'}
# plt.pie(marks,labels=classes,colors=colors,autopct='%0.2f%%',explode=explode_values,textprops=textprops)
# plt.title('Subjects and Average Scores')
# plt.legend()
# plt.show()

# df=pd.read_csv('./matplotlib/SUPERMARKET.csv')
# print(df.head())

# payment_df=pd.DataFrame(df['Payment'].value_counts())
# print(payment_df)
# plt.pie(payment_df['count'],labels=payment_df.index,colors=['red','blue','green'],autopct='%0.2f%%')
# plt.show()