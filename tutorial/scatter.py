import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Set seed for reproducibility
np.random.seed(42)

# Generate random data
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# Create scatter plot
data = [go.Scatter(
    x=random_x, 
    y=random_y, 
    mode='markers', 
    marker=dict(
        size=12,
        color="rgb(51,145,152)",
        symbol="pentagon",
        line={"width":2}
    )
)]

# Designing the layout
layout = go.Layout(
    title="Hello First Plot",
    xaxis=dict(title="My X Axis"),
    yaxis=dict(title="My Y Axis")
)

# Create a figure
fig = go.Figure(data=data, layout=layout)

# Plot the data
pyo.plot(fig, filename="tutorial.html")
