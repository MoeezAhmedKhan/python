# Essential Subplot functions in Matplotlib

# What is subplot?
# Subplot is used to show multiple plots (charts) in a single figure (canvas).

import matplotlib.pyplot as plt

# plt.subplot(num_of_rows, num_of_columns, index)
# rows = total rows of plots
# columns = total columns of plots
# index = position number of current plot (starts from 1)

x = [1, 2, 3, 4]
y = [10, 30, 20, 40]

plt.subplot(1, 2, 1)  # (1 row, 2 columns, 1st plot) → Left side
plt.plot(x, y)
plt.title("Line Chart")

plt.subplot(1, 2, 2)  # (1 row, 2 columns, 2nd plot) → Right side
plt.bar(x, y)
plt.title("Bar Chart")

plt.show()
