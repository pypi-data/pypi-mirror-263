def set_plot_style(style='default'):
    """
    Set the plotting style for visualizations.
    
    Parameters:
    - style (str): The style name. Options include 'default', 'ggplot', 'seaborn', etc.
    """
    import matplotlib.pyplot as plt
    plt.style.use(style)
    

def save_fig(fig, filename, dpi=300):
    """
    Save the figure to a file.
    
    Parameters:
    - fig (matplotlib.figure.Figure): The figure object to save.
    - filename (str): The filename or path to save the figure to.
    - dpi (int): The resolution in dots per inch.
    """
    fig.savefig(filename, dpi=dpi)


def show_available_styles():
    """
    Print available plotting styles.
    """
    import matplotlib.pyplot as plt
    print("Available styles:")
    print(plt.style.available)