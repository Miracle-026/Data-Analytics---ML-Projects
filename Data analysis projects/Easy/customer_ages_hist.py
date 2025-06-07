import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/Users/DEKATECH/Data analysis projects/Easy/customer_data.csv")
print(data.head())
print(data.columns)
print(data.isnull().sum())
print(data.describe())

sns.set(style='whitegrid')
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=20, kde=True, color='blue')
plt.title('Distribution of Customer Ages', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.show()