# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
sns.set(color_codes = True)
import seaborn as sns

df=pd.read_csv('/content/enhanced_zomato_dataset_clean.csv')
print(df.head())
print(df.tail())

df.shape

df.info

df.describe()

df.dtypes

duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows:", duplicate_rows_df.shape)
df.count()

df=df.drop_duplicates()
df.head()
df.count()

print(df.isnull().sum())
df=df.dropna()
df.count()

sns.boxplot(x=df['Avg_Price_Cuisine'])

sns.boxplot(x=df['Best_Seller'])

sns.boxplot(x=df['Avg_Price_Restaurant'])
df.Average_Rating.value_counts().nlargest(20).plot(kind='bar')

cor=df.select_dtypes(include=np.number).corr()
cor
plt.figure(figsize=(10,10))
sns.heatmap(cor,annot=True)

plt.subplots()
plt.scatter(df['Avg_Price_Cuisine'],df['Avg_Price_Restaurant'])
