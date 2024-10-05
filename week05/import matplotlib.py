import matplotlib.pyplot as plt

# Data from the screenshot
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
calories = [2130, 2203, 2621, 2758, 1000, 1900, 2900, 3221, 3371, 3350]
fiber = [12, 15, 21, 30, 10, 14, 29, 38, 40, 39]
potassium = [840, 1421, 1981, 2432, 500, 1203, 2931, 3290, 3375, 3212]

# Create a line chart
plt.figure(figsize=(10, 6))
plt.plot(days, calories, label='Calories', marker='o', color='blue')
plt.plot(days, fiber, label='Fiber (g)', marker='o', color='green')
plt.plot(days, potassium, label='Potassium (mg)', marker='o', color='orange')

# Adding titles and labels
plt.title('Calories, Fiber, and Potassium Intake Over 10 Days')
plt.xlabel('Days')
plt.ylabel('Intake')
plt.legend()

# Show plot
plt.grid(True)
plt.show()