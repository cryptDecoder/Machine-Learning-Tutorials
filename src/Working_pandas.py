import pandas as pd
import matplotlib.pyplot as plt

# pandas datatypes
# 1: Series : 1 -dimeansional

series = pd.Series(['AUDI', "HONDA", "BMW"])
print(series)

colors = pd.Series(["Red", "Orange", "Blue"])
print(colors)
# 2: 2-D dimensional

cars_data = pd.DataFrame({"Car makes :": series, "Color :": colors})
print(cars_data)

# Import Data
print(" --- reading data from csv ---")
heart_data = pd.read_csv("../data/datasets_33180_43520_heart.csv")
print(heart_data)

# exporting data
heart_data.to_csv("new_exported_data.csv", index=False)

# Describe the Data
print("--- Describing the data ---")
print(heart_data.dtypes)
print(heart_data.columns)
print(heart_data.index)
print(heart_data.describe())
print(heart_data.info())
print(heart_data["age"].sum())
print(len(heart_data))

# Selecting and Viewing the data
print(heart_data.head())

# .loc and .iloc

animals = pd.Series(["CAT", "DOG", "TIGER", "MOUSE"])
print(animals)

print(animals.loc[1])

print(heart_data.loc[3])

# iloc referese the possition

print(animals.iloc[2])

# slicing
print(animals.iloc[:3])
print(heart_data.iloc[:5])
print(heart_data.age)
print(heart_data[heart_data["age"] < 54])

print(pd.crosstab(heart_data['age'], heart_data['sex']))
print(heart_data.groupby(['sex']).mean())

heart_data['age'].hist()
# plt.show()

# manipulating data
heart_data['age'].fillna(heart_data['age'].mean(), inplace=True)
heart_data.dropna()


