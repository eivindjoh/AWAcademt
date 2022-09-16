import pandas as pd
import plotly.express as px
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

df = pd.read_csv(r"C:\Users\Eivin\OneDrive\Skrivebord\Student Mental health.csv")

header_text = html.H1(children='Students Mental Health', style={
            'color': colors['text'],
            'font-size': 50
        }, className='app-header-text u-pull-left')

header_logo = html.Img(src=LOGO_PATH, className='app-header-img u-pull-right', height=125)
header = html.Div([header_text, header_logo], className='app-header row')

age_distribution = px.histogram(df, x='Age', title='Age Distribution')
course = px.histogram(df, x='What is your course?', title='Course Distribution')
sex = px.pie(df, names='Choose your gender', title='Gender distribution')

my_plot1 = dcc.Graph(id='age_distribution')
my_plot2 = dcc.Graph(figure=course, id='course')
my_plot3 = dcc.Graph(figure=sex, id='sex')

depressed_menu = dcc.Checklist(options=[
       {'label': 'Depressed', 'value': 'Yes'},
       {'label': 'Not Depressed', 'value': 'No'},
   ], id='depressed_menu')

anxiety_menu = dcc.Checklist(options=[
       {'label': 'Anxious', 'value': 'Yes'},
       {'label': 'Not Anxious', 'value': 'No'},
   ], id='anxious_menu')


@app.callback(
    dash.dependencies.Output('age_distribution', 'figure'),
    [dash.dependencies.Input('depressed_menu', 'value'),
     dash.dependencies.Input('anxious_menu', 'value')]
)
def age_distribution(menu_depr, menu_anx):
    if menu_depr and not menu_anx:
        tdf = df.where(df['Do you have Depression?'] == menu_depr[0])
        plot = px.histogram(tdf, x='Age', title=f'Age Distribution Depressed: {menu_depr[0]}')
    elif menu_depr and menu_anx:
        tdf = df.where((df['Do you have Depression?'] == menu_depr[0]) & (df['Do you have Anxiety?'] == menu_anx[0]))
        plot = px.histogram(tdf, x='Age', title=f'Age Distribution Depressed: {menu_depr[0]} Anxiety: {menu_anx[0]}')
    elif menu_anx and not menu_depr:
        tdf = df.where(df['Do you have Anxiety?'] == menu_anx[0])
        plot = px.histogram(tdf, x='Age', title=f'Age Distribution Anxiety: {menu_anx[0]}')
    else:
        plot = px.histogram(df, x='Age', title='Age Distribution')
    return plot


@app.callback(
    dash.dependencies.Output('sex', 'figure'),
    [dash.dependencies.Input('depressed_menu', 'value'),
     dash.dependencies.Input('anxious_menu', 'value')]
)
def sex_distribution(menu_depr, menu_anx):
    if menu_depr and not menu_anx:
        tdf = df.where(df['Do you have Depression?'] == menu_depr[0])
        plot = px.pie(tdf, names='Choose your gender', title=f'Gender distribution Depressed: {menu_depr[0]}')
    elif menu_depr and menu_anx:
        tdf = df.where((df['Do you have Depression?'] == menu_depr[0]) & (df['Do you have Anxiety?'] == menu_anx[0]))
        plot = px.pie(tdf, names='Choose your gender', title=f'Gender distribution Depressed: {menu_depr[0]} Anxiety: {menu_anx[0]}')
    elif menu_anx and not menu_depr:
        tdf = df.where(df['Do you have Anxiety?'] == menu_anx[0])
        plot = px.pie(tdf, names='Choose your gender', title=f'Gender distribution Anxiety: {menu_anx[0]}')
    else:
        plot = px.pie(df, names='Choose your gender', title='Gender distribution')
    return plot


app.layout = html.Div(children=[header, html.Div([depressed_menu, anxiety_menu, my_plot1, my_plot2, my_plot3])])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)

