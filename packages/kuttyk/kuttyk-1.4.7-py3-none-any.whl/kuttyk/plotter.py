import matplotlib.pyplot as plt
import numpy as np

def simple_line_plot(x, y, title='Simple Line Plot', xlabel='X-axis', ylabel='Y-axis'):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def advanced_plot(x, y):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    axs[0, 0].scatter(x, y)
    axs[0, 0].set_title('Scatter Plot')
    axs[0, 1].plot(x, y, 'tab:orange')
    axs[0, 1].set_title('Line Plot')
    axs[1, 0].bar(x, y, color='tab:green')
    axs[1, 0].set_title('Bar Plot')
    axs[1, 1].hist(y, bins=5, color='tab:red')
    axs[1, 1].set_title('Histogram')
    for ax in axs.flat:
        ax.set(xlabel='x', ylabel='y')
        ax.label_outer()
    plt.tight_layout()
    plt.show()