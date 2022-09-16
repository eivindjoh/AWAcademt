import plotly.express as px
import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

x = [0, 1, 2, 3, 4]
y = [5, 3, 2, 7, 12]

header = header_text = html.H1(children='Checkpoint Dash', style={
            'font-size': 50
        })

fig = px.line(x=x, y=y)
fig.show()

radio_button = dcc.RadioItems(options=[0, 1, 2, 3, 4], id='radio')
slider = dcc.Slider(min=0, max=30, step=1, value=10, id='slider')

plot = dcc.Graph(id='lineplot')

@app.callback(
    dash.dependencies.Output('lineplot', 'figure'),
    [dash.dependencies.Input('radio', 'value'),
     dash.dependencies.Input('slider', 'value')]
)
def update_lineplot(radio_value, slider_value):
    x_values = [0, 1, 2, 3, 4]
    y_values = [5, 3, 2, 7, 12]
    if radio_value == 0:
        y_values[radio_value] = slider_value
        print(y_values)
    if radio_value:
        y_values[radio_value] = slider_value
        print(y_values)
    figure = px.line(x=x_values, y=y_values)
    return figure


app.layout = html.Div([header, plot, radio_button, slider])
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
