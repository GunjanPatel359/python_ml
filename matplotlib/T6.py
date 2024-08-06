import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('dark_background')

study_hours=[2,3,4,4,5,6,7,7,8,9,9,10,11,11,12]
marks=[6,10,15,20,34,44,55,60,55,67,70,80,90,99,100]

# plt.scatter(study_hours,marks)
# plt.show()

# plt.plot(study_hours,marks,'r--')
# plt.show()

# plt.hist(marks)

# plt.figure(figsize=(6,6))
# plt.plot(study_hours,marks,'r-')
# plt.plot(study_hours,marks,'bo')
# plt.show()

plt.figure(figsize=(6,6))
plt.subplot(2,2,1)
plt.scatter(study_hours,marks)
plt.subplot(2,2,2)
plt.plot(study_hours,marks,'r-')
plt.subplot(2,2,3)
plt.hist(marks)
plt.subplot(2,2,4)
plt.plot(study_hours,marks,'r-')
plt.plot(study_hours,marks,'bo')
plt.savefig('./matplotlib/subplot.png',facecolor='k')
plt.show()
