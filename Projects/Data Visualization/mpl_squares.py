import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# print(plt.style.available)
plt.style.use('seaborn')

# fig: Entire figure = collections of plots, ax = single plot in the figure
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set the title and label
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()