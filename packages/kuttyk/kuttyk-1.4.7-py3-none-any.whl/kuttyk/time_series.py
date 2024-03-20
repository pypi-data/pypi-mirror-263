import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def time_series_plot(dates, values, title='Time Series Plot', xlabel='Date', ylabel='Value'):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, values, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Setting up the date format for the x-axis
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    
    plt.gcf().autofmt_xdate()  # Rotate date labels to prevent overlap
    plt.grid(True)
    plt.show()
