import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Example data: list of lists of 2D coordinates
coordinates = [
    [(1, 2), (2, 3), (3, 4)],
    [(4, 5), (5, 6), (6, 7)],
    [(7, 8), (8, 9), (9, 10)]
]

# Initial index
index = [0]

# Plot the initial scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(*zip(*coordinates[index[0]]))
plt.subplots_adjust(bottom=0.2)

# Function to update the plot
def update_plot():
    ax.clear()
    scatter = ax.scatter(*zip(*coordinates[index[0]]))
    plt.draw()

# Callback functions for the buttons
def next(event):
    if index[0] < len(coordinates) - 1:
        index[0] += 1
    update_plot()

def prev(event):
    if index[0] > 0:
        index[0] -= 1
    update_plot()

# Adding "Next" button
ax_next = plt.axes([0.8, 0.05, 0.1, 0.075])
btn_next = Button(ax_next, 'Next')
btn_next.on_clicked(next)

# Adding "Previous" button
ax_prev = plt.axes([0.7, 0.05, 0.1, 0.075])
btn_prev = Button(ax_prev, 'Previous')
btn_prev.on_clicked(prev)

plt.show()
