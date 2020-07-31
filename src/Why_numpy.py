import pandas as pd
import numpy as np

# Datatypes and Attributes

a1 = np.array([1, 2, 3, 5])
print(a1)

a2 = np.array([[[1, 2, 3], [2, 3, 4]], [[3, 4, 5],
                                        [4, 5, 6]], [[5, 6, 7], [6, 7, 8]]])
print(a2)
print(a2.shape)
print(a1.ndim, a2.ndim)
print(a1.dtype, a2.dtype)
print(a1.size, a2.size)
print(type(a1))

a3 = np.array([[1, 2, 4], [4, 5, 6]])
df = pd.DataFrame(a3)
print(df)

name = np.array([['First Name', 'Last Name', 'City', 'Zip Code'], [
                'Jacke', 'Jonas', 'New', 785256]])
print(name)
names = pd.DataFrame(name)
print(names)

# Creating Array

a4 = np.array([1, 2, 3])
print(a4)
print(a4.dtype)
ones = np.ones((2, 3), dtype=int)
print(ones)

zeros = np.zeros((2, 3))
print(zeros)

range_aaray = np.arange(1, 10, 2)
print(range_aaray)

random_aaray = np.random.random((5, 3))
print(random_aaray)

# Pesudo random numbers seed
print("--------------------------------")
np.random.seed(seed=0)
random_aaray_4 = np.random.randint(10, size=(5, 3))
print(random_aaray_4)

# viewing arrays and metrics
print("------------------------------------------------------")
print(np.unique([1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 67, 8, 9, 5]))

print(random_aaray_4[:2, :2])
print("------")

# Arithmetic
a1 = np.array([1, 2, 3, 4])
ones = np.ones(4)
print(ones)
print(a1 + ones)
print(np.square(a1))

# reshaping and transposing
print("---------------")
print(a3.shape)
print(a3.reshape(2, 3, 1))


# Dot product example

sales_ammount = np.random.randint(20, size=(5, 3))
print(sales_ammount)

# weekly sales dataframe

weekly_sales = pd.DataFrame(
    sales_ammount, index=["Mon", "Tues", "Wed", "Thurs", "Fri"],
    columns=["Almond Butter", "Peanut Butter", "Cashew Butter"])

# Create prices
prices = np.array([10, 8, 12])

butter_prices = pd.DataFrame(prices, index=['Price'], columns=[
                             "Almond Butter", "Peanut Butter", "Cashew Butter"])
