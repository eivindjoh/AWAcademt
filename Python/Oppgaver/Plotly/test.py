import pandas as pd
import plotly.express as px


x = [1, 2, 3, 4, 5]
y = [5, 9, 10, 2, 3]

fig = px.line(x=x, y=y)
fig.show()
