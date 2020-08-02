import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7]
y = [5, 6, 7, 8, 9, 0, 3]


plt.plot(x, y)
# plt.show()

fig, ax = plt.subplots()
ax.plot(x, y)
# plt.show()


# Matplotlib example workfloew

x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 7, 8]

fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(x, y)
ax.set(title="Simple Plot", xlabel="X-axix", ylabel="Y-axis")
#fig.savefig("../../images/sample_plot.png")
