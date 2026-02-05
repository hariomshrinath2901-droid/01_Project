import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df= pd.read_csv('data1.csv')
x =df["Marks"]
y=df["Age"]
plt.scatter(x,y)
plt.xlabel("Marks")
plt.ylabel("Age")
plt.title("data")
plt.show()
