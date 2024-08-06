import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('dark_background')
rollno=[1,2,3,4,5,6,7,8,9,10]
marks=[10,20,30,40,50,60,70,80,90,100]

# plt.plot(rollno,marks,'r-')
# plt.show()

# plt.plot(rollno,marks,linestyle='-')
# plt.show()

# plt.plot(rollno,marks,linestyle='--',color='#708569')
# plt.show()

# plt.plot(rollno,marks,linestyle=':',color='orange')
# plt.show()

# plt.plot(rollno,marks,linestyle='-',linewidth=1.5 )
# plt.show()

study_hours=[2,3,4,4,5,6,7,7,8,9,9,10,11,11,12,]
marks=[6,10,15,20,34,44,55,60,55,67,70,80,90,99,100]

# plt.figure(figsize=(8,8))
# plt.xticks(np.arange(0,15,1))
# plt.yticks(np.arange(0,100,5))
# plt.plot(study_hours,marks,'r-')
# plt.xlabel('Study Hours')
# plt.ylabel('Marks')
# plt.show()

# plt.figure(figsize=(8,8))
# plt.xticks(np.arange(0,15,1))
# plt.yticks(np.arange(0,100,5))
# plt.plot(study_hours,marks,'r-')
# plt.plot(study_hours,marks,'bo')
# plt.xlabel('Study Hours')
# plt.ylabel('Marks')
# plt.show()