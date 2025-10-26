# Practice with scnerios

import numpy as np
import matplotlib.pyplot as plt

# Restaurant Data [restaurant_id, 2020, 2021, 2022, 2023, 2024]
restaurant_sales = np.array([
    [1, 25000, 27000, 26000, 30000, 28000],
    [2, 18000, 19000, 21000, 20000, 22000],
    [3, 30000, 32000, 31000, 33000, 35000],
    [4, 15000, 16000, 15500, 17000, 16500],
    [5, 4000, 42000, 41000, 43000, 44000],
])

print(restaurant_sales[:,1:]) # : (All rows) 1: Columns starting from index 1 (skip column 0 = ID) 

# Get Total Sales Per Year

yearlySale = np.sum(restaurant_sales[:,1:]) # Skip Ids then total
print(f"Total Yearly Sale (without IDs): {yearlySale}")

yearlySale = np.sum(restaurant_sales[:,1:], axis=1) # axis = 1 (Sum row wise)
print(f"Total Yearly Sale (without IDs) Row Wise: {yearlySale}")

yearlySale = np.sum(restaurant_sales[:,1:], axis=0) # axis = 0 (Sum column wise)
print(f"Total Yearly Sale (without IDs) Column Wise: {yearlySale}")

# Get Min Sale
minSale = np.min(restaurant_sales[:,1:], axis=1) # axis = 1 (Min row wise)
print(f"Min Sale (without IDs) Row Wise: {minSale}")

# Get avg sale of each restaurant
avg = np.mean(restaurant_sales[:,1:], axis=1) # axis = 1 (avg row wise)
print(f"Avg Restaurant Sale Row Wise: {avg}")

# Cumulative Sum
cum_sum = np.cumsum(restaurant_sales[:,1:], axis=1) # cumsum mean add into previous one || axis = 1 (cumsum row wise)
print(f"Cumulative Sum Row Wise: \n{cum_sum}")


# Now We just plot cunsum into Matplotlib

plt.figure(figsize=(8,8))
plt.plot(np.mean(cum_sum, axis=0))
plt.title("Average of Cumulative Sum")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.show()