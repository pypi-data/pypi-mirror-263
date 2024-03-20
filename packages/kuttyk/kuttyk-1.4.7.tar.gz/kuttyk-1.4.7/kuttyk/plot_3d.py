import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d(x, y, z, plot_type='scatter', title='3D Plot', xlabel='X-axis', ylabel='Y-axis', zlabel='Z-axis'):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    if plot_type == 'scatter':
        ax.scatter(x, y, z, c='r', marker='o')
    elif plot_type == 'line':
        ax.plot(x, y, z, color='b')
    else:
        print('Unsupported plot type.')
        return
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.show()
