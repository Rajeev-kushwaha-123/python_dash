import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo
df=pd.read_csv("data.csv")
df2=df[df["ecode"]=="1098"]
df2.set_index("ename",inplace=True)
list=[col for col in df2.columns if col.startswith('s')]
df2=df2[list]
data=[go.Scatter(x=df2.columns,y=df2.loc[name],mode='lines',name='name') for name in df2.index]
pyo.plot(data)
