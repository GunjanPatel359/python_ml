import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('dark_background')

marks_50_students=np.random.randint(0,100,(50))
print(marks_50_students)

# plt.hist(marks_50_students)
# plt.show()

# bins=np.arange(0,100,5)
# plt.figure(figsize=(6,6))
# plt.hist(marks_50_students,bins=bins)
# plt.xticks(np.arange(0,100,5))
# plt.show()

# bins=np.arange(0,100,5)
# plt.figure(figsize=(6,6))
# plt.hist(marks_50_students,bins=bins,color='orange')
# plt.xticks(np.arange(0,100,5))
# plt.show()

# bins=np.arange(0,100,5)
# plt.figure(figsize=(6,6))
# plt.hist(marks_50_students,bins=bins,color='orange',orientation='horizontal')
# plt.xticks(np.arange(0,100,5))
# plt.show()

# bins=np.arange(0,100,5)
# plt.figure(figsize=(6,6))
# plt.hist(marks_50_students,bins=bins,color='orange',orientation='horizontal')
# plt.yticks(np.arange(0,100,5))
# plt.show()

# bins=np.arange(0,100,5)
# plt.figure(figsize=(6,6))
# plt.hist(marks_50_students,bins=bins,color='orange',rwidth=0.6)
# plt.xticks(np.arange(0,100,5))
# plt.show()

# bins=np.arange(0,100,5)
# plt.figure(figsize=(6,6))
# plt.hist(marks_50_students,bins=bins,color='orange',histtype='step')
# plt.xticks(np.arange(0,100,5))
# plt.show()


# marks_50_students1=np.random.randint(0,100,(50))
# marks_50_students2=np.random.randint(0,100,(50))
# bins=np.arange(0,100,5)
# plt.figure(figsize=(6,6))
# plt.hist([marks_50_students1,marks_50_students2],bins=bins,color=['orange','blue'])
# plt.xticks(np.arange(0,100,5))
# plt.xlabel('Marks')
# plt.ylabel('Frequency')
# plt.title('Marks of students of 2 Classes')
# plt.show()
 
 