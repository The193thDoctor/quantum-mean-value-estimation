import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)  # Values to map to colors
print(colors)

# Create a figure and axis
fig, ax = plt.subplots()
cmap = plt.get_cmap('tab10')
print(cmap(0.1))
print(cmap(int(1)))
print(cmap(float(1)))
print(cmap(1.0))

# Scatter plot with a colormap
scatter = ax.scatter(x, y, c=colors, cmap='tab10')

# Add a colorbar to show the color scale
colorbar = plt.colorbar(scatter, ax=ax)

# Show the plot
plt.show()