import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go
np.random.seed(42)
x_values=np.linspace(0,100,100)
y_values=np.random.randn(100)
trace=go.Scatter(
                 x=x_values,y=y_values,
                 mode="markers",
                 name="marker")
trace1=go.Scatter(
    x=x_values,y=y_values+4,
    mode="lines",
    name="linechart"
)
trace2=go.Scatter(
    x=x_values,y=y_values-5,
    mode="lines+markers" ,name="favourate"
)
data=[trace,trace1,trace2]
layout=go.Layout(title='line charts')
fig=go.Figure(data=data , layout=layout)
pyo.plot(fig ,filename="linechat.html")

