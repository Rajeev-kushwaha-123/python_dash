import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

# Read the CSV file
df = pd.read_csv("copy.csv")

# Print the DataFrame
print(df)

# Create a simple bar plot of salaries
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df['ename'],
    y=df['salary'],
    name='Salary'
))

# Update the layout of the plot
fig.update_layout(
    title='Salaries of Employees',
    xaxis_title='Employee Name',
    yaxis_title='Salary',
    barmode='group'
)

# Show the plot
pyo.plot(fig)
