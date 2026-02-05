import pandas as pd
df= pd.read_csv('data1.csv')
average= df["Marks"].mean()
print("Average Marks",average)

