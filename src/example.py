import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../data/datasets_33180_43520_heart.csv")
print("--- Following Table shows heart disease information ---")
print(df.head())

print(df.target.value_counts().plot(kind="bar"))
#plt.show()

# 1: Problem Definition predict heart disesses
