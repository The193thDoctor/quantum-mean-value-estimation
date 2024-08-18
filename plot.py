import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

matplotlib.use("TkAgg")

cmap = plt.get_cmap('tab10')

index = 0

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


    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)

    def update_plot(reals, imags):
        ax.clear()
        ax.scatter(reals, imags, s=100)
        plt.draw()


    print(reals[0])
    print('hi')
    print(imags[0])
    print(reals)

    def next(event):
        global index
        if index < num_iterations:
            index += 1
        update_plot(reals[index], imags[index])

    def prev(event):
        global index
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

    plt.show()



