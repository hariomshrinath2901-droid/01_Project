import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data1.csv")

plt.figure()
correlation = df.select_dtypes(include='number').corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()