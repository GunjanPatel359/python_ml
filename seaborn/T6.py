import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

penguins=sns.load_dataset('penguins')
print(penguins.head())

# plt.figure(figsize=(12,12))
# sns.pairplot(penguins)
# plt.show()

# plt.figure(figsize=(12,12))
# sns.pairplot(penguins,hue='sex',palette='Reds')
# plt.show()

# plt.figure(figsize=(12,12))
# sns.pairplot(penguins,hue='species',palette='Blues')
# plt.show()

# plt.figure(figsize=(12,12))
# sns.pairplot(penguins,kind='kde',palette='Greens')
# plt.show()

# plt.figure(figsize=(12,12))
# sns.pairplot(penguins,kind='hist',palette='Greens')
# plt.show()

# plt.figure(figsize=(12,12))
# sns.pairplot(penguins,hue='species',diag_kind='hist',palette='rainbow')
# plt.show()

# plt.figure(figsize=(12,12))
# sns.pairplot(penguins,corner=True)
# plt.show()

# plt.figure(figsize=(12,12))
# sns.pairplot(penguins,hue='species',markers=['o','s','D'],palette='inferno')
# plt.show()
