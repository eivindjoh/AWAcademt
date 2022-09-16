import plotly.express as px
import plotly.express.data
import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

header = html.H1(children='Hello Dashboard')

city_dropdown_options = [
    {'label': 'New York City', 'value': 'NYC'},
    {'label': 'Montreal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'}
]

df = plotly.express.data.tips()
print(df)
tips = px.scatter(df,
                  x='total_bill', y='tip', title='Tips male/female',
                  trendline='ols', color='sex', marginal_x='box',
                  marginal_y='violin'
                  )
my_plot = dcc.Graph(figure=tips)

city_dropdown = dcc.Dropdown(options=city_dropdown_options, value='MTL')

app.layout = html.Div([header, city_dropdown, my_plot])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)


