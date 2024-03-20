import seaborn as sns
import matplotlib.pyplot as plt

def heatmap_plot(data, title='Heatmap', xlabel='X-axis', ylabel='Y-axis', xticklabels=[], yticklabels=[]):
    plt.figure(figsize=(8, 6))
    sns.heatmap(data, annot=True, fmt='.2f', cmap='coolwarm', xticklabels=xticklabels, yticklabels=yticklabels)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
