import plotly.graph_objects as go

def plot_geo_locations(latitudes, longitudes, titles=None):
    fig = go.Figure(data=go.Scattergeo(
        lon = longitudes,
        lat = latitudes,
        text = titles,
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'circle',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Blues',
            cmin = 0,
            colorbar_title="Location Markers"
        )))

    fig.update_layout(
        title = 'Global Location Markers',
        geo = dict(
            scope = 'world',
            projection_type = 'orthographic',
            showland = True,
            landcolor = "rgb(212, 212, 212)",
            subunitcolor = "rgb(255, 255, 255)",
            countrycolor = "rgb(255, 255, 255)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )
    fig.show()
    