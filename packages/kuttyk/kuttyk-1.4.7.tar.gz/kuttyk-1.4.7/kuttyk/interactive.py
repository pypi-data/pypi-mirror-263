def interactive_plot(x, y):
    import plotly.graph_objects as go

    # Creating a Plotly figure
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers+lines', name='Data',
                                    marker=dict(size=10, color='rgba(152, 0, 0, .8)',
                                                line=dict(width=2, color='rgb(0, 0, 0)'))))
    # Adding layout information
    fig.update_layout(title='Interactive Plot',
                      xaxis_title='X-axis',
                      yaxis_title='Y-axis')
    # Display the figure
    fig.show()
