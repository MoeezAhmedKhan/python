# Matplotlib is used for data visualization

# Problem Statement:
# Suppose we have monthly sales data for a whole year and we want to find out which month had the highest sales.
# Manually checking and comparing the numbers would be time-consuming and prone to errors. 
# By using Matplotlib, we can create a visual representation of the sales data, 
# making it easy to identify trends and quickly determine the month with the highest sales.

# Data Visualization:
# The process of representing raw data visually using charts or graphs, 
# such as bar charts, line charts, etc., to make it easier to understand and analyze.

# Matplotlib provides several types of graphs:
# Line Graph, Bar Chart, Pie Chart, Histogram, Scatter Plot, Custom Graphs

import matplotlib.pyplot as plt

# Plot a Line Graph
# To plot a graph, we need x-axis and y-axis values as list/array

xList = [1, 2, 3, 4]
yList = [10, 20, 10, 25]

plt.plot(xList, yList)  # Plot the line graph
plt.show()  # This renders the graph on the screen; it is required to call this

# Key Terms We Should Know:

# 1. Data Point - a single pair of x and y values in the dataset, e.g. (2, 5) where x = 2 and y = 5.
# 2. X-axis / Y-axis - Horizontal and vertical axes of the graph
# 3. Figure - The canvas where the graph is plotted
# 4. Axes - The actual area in the figure where the graph is drawn
# 5. Plot - The visual representation of data (line, bar, etc.)
# 6. Marker - Symbol or dot representing individual data points
# 7. Line Style - Defines how the line will be drawn (solid, dashed, dotted)
# 8. Color - Color of the line or plot
# 9. Legend - Explains what each line or color represents
# 10. Label - Text describing the x-axis and y-axis
# 11. Title - Headline or name of the graph
# 12. Grid - Optional grid lines to make the graph easier to read
# 13. Function - A block of reusable code
# 14. Method - A function that belongs to an object
# 15. Parameters - Inputs to a function or method
# 16. Keyword Arguments - Named inputs passed to functions/methods
# 17. Object-Oriented API - Using classes and objects to create plots
# 18. DPI (Dots Per Inch) - Resolution of the figure
# 19. Backend - The rendering engine used by Matplotlib

x = ['Monday','Tuesday','Wednesday','Thursday','Friday']
y = [1010, 2000, 889, 55, 400]

plt.plot(x, y)
plt.title("Bakery Sales This Week")
plt.xlabel("Days of the week")
plt.ylabel("Sales Per day")
plt.show()

# Now Understand About Plot Which Argment can takes Plot fuction
# It is used to create Line Chart

month = [1, 2, 3, 4]
sales = [1111,2122,1001,1000] 

plt.plot(month, sales, color='blue', linestyle='--', linewidth=2, marker='o', label='2025 Sales Data')
plt.xlabel("Months")
plt.ylabel("Sales Data")
plt.title("Monthly Sales Data")
plt.legend(loc='upper left', fontsize=7) # It show plot label (2025 Sales Data) on the graph
plt.grid(color="red", linestyle=":", linewidth=1)
plt.xlim(1,4) # How much of the X-axis you want to show (from 1 to 4).
plt.ylim(0, 2122) # How much of the Y-axis you want to show (from 0 to 2122).
plt.xticks(month, ["1st Month", "2nd Month", "3rd Month", "4th Month"])  # Clear labels on X-axis
plt.yticks(sales, [f"${i}" for i in sales])  # only shows ticks at your data points
plt.show()


# Now:
# Bar Charts, Histogram, And Pie Chart is commonly used Chart

# Bar Charts:
# Bar chart is used to compare different items or categories by showing their values as vertical or horizontal bars, making it easy to see which item is bigger or smaller.
# plt.bar(x, height, color='color name', width = value, marker='o', label='label here') - Syntax

product = ['A Product', 'B Product', 'C Product', 'D Product', 'E Product']
sales = [1800, 1100, 800, 400, 2000]
plt.bar(product, sales, color = "lightblue", label="Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales Data")
plt.title("Product Sales Data")
plt.legend()
plt.grid(color="red", linestyle=":", linewidth=2)
plt.show()


# Pie Chart:
# Pie chart is used to show how different parts contribute to the whole, with each slice representing a percentage of the total, making it easy to understand the proportion of each part
# values → Numbers for slice sizes (e.g., revenue).
# labels → Names for each slice (e.g., region names).
# autopct → (Shows each slice as a percentage of the total) inside the slice.

# plt.pie(value, label="label here", color="color name", autopc-"%1.1f%%") -Syntax

region = ["North", "South", "East", "West"]
revenue = [1000, 700, 2000, 1200]
plt.pie(revenue, labels=region, autopct="%1.1f%%", colors=['gold','lightgreen','lightblue','coral'])
plt.title("Revenue Contribution By Region")
plt.show()


