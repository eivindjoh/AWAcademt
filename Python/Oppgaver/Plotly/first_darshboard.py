import os
import pandas as pd
import plotly.express as px
import plotly.express.data
import dash
from dash import dcc
from dash import html

LOGO_PATH = r'https://www.fhi.no/contentassets/c03aa76fe30941f08474ee823ba2a928/logo_kort.png'
CSS_URL = r'https://codepen.io/chriddyp/pen/bWLwgP.css'


app = dash.Dash(__name__, external_stylesheets=[CSS_URL])

colors = {
    'background': '#111111',
    'text': '#393c61'
}

df = pd.read_csv(r"C:\Users\Eivin\OneDrive\Skrivebord\Monkeypox.csv")

confirmed_cases = px.histogram(df, x='Date_confirmation', title='Total confirmed cases')
symptoms = px.histogram(df, x='Symptoms', title='Symptoms')
location = px.histogram(df, x='Country', title='Cases per Country')
my_plot1 = dcc.Graph(figure=confirmed_cases, id='confirmed_cases')
my_plot2 = dcc.Graph(figure=symptoms, id='symptoms')
my_plot3 = dcc.Graph(figure=location, id='location')

header_text = html.H1(children='Monkeypox', style={
            'color': colors['text'],
            'font-size': 80
        }, className='app-header-text u-pull-left')

header_logo = html.Img(src=LOGO_PATH, className='app-header-img u-pull-right', height=125)
header = html.Div([header_text, header_logo], className='app-header row')

city_dropdown = dcc.Dropdown(df.Country.unique(), id='dropdown', value=df['Country'])


@app.callback(
    dash.dependencies.Output('confirmed_cases', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def update_confirmed_cases(dropdown_value):
    if not dropdown_value:
        confirmed = px.histogram(df, x='Date_confirmation', title='Total confirmed cases')
    else:
        tdf = df.where(df['Country'] == dropdown_value)
        confirmed = px.histogram(tdf, x='Date_confirmation', title='Total confirmed cases')
    return confirmed


app.layout = html.Div(children=[header, html.Div([city_dropdown, my_plot1, my_plot2, my_plot3])])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)

