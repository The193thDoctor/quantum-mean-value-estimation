import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

matplotlib.use("TkAgg")

cmap = plt.get_cmap('tab10')

_RADIUS = 1.2

# '1d' refers to the fact we are estimating mean of single variable
def plot1d(state_vectors):
    if len(state_vectors[0]) == 0:
        ValueError('state_vectors is empty')
        return

    state_vectors = np.array(state_vectors)  # Convert to numpy array for easier manipulation
    num_iterations = len(state_vectors) - 1
    num_qubits = int(np.log2(len(state_vectors[0])))
    num_elements = np.pow(2, num_qubits)

    state_vectors *= np.sqrt(num_elements) # scale the state vector
    reals = np.real(state_vectors)
    imags = np.imag(state_vectors)
    index = 0
    colors = np.arange(num_elements) % 10

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)

    def update_plot(reals, imags):
        ax.clear()
        for i in range(num_elements):
            ax.plot([0, reals[i]], [0, imags[i]], color=cmap(i % 10))
        ax.scatter(reals, imags, c=colors, cmap='tab10', s=100)
        ax.text(0.95, 0.95, f'Index: {index}',
                transform=ax.transAxes, fontsize=12,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(facecolor='white', alpha=0.5, edgecolor='black'))
        ax.set_xlim(-_RADIUS, _RADIUS)
        ax.set_ylim(-_RADIUS, _RADIUS)
        plt.draw()


    def next(event):
        nonlocal index
        if index < num_iterations:
            index += 1
        update_plot(reals[index], imags[index])

    def prev(event):
        nonlocal index
        if index > 0:
            index -= 1
        update_plot(reals[index], imags[index])

    # Adding "Next" button
    ax_next = plt.axes((0.8, 0.05, 0.1, 0.075))
    btn_next = Button(ax_next, 'Next')
    btn_next.on_clicked(next)

    # Adding "Previous" button
    ax_prev = plt.axes((0.7, 0.05, 0.1, 0.075))
    btn_prev = Button(ax_prev, 'Previous')
    btn_prev.on_clicked(prev)

    for i in range(num_elements):
        ax.plot([0, reals[index][i]], [0, imags[index][i]], color=cmap(i % 10))
    ax.scatter(reals[index], imags[index], c=colors, cmap='tab10', s=100)
    ax.text(0.95, 0.95, f'Index: {index}',
            transform=ax.transAxes, fontsize=12,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(facecolor='white', alpha=0.5, edgecolor='black'))
    ax.set_xlim(-_RADIUS, _RADIUS)
    ax.set_ylim(-_RADIUS, _RADIUS)
    plt.show()



