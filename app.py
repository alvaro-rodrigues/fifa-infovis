import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from src.transformations import transform1, transform2
from src.plot import plot1, plot2

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'FIFA Data Visualization'

df = pd.read_csv("./input/players_20.csv")
fig1 = plot1(transform1(df))
fig2 = plot2(transform2(df))

app.layout = html.Div(
    html.Div([
        html.Div([
            html.H1(children='FIFA Data Visualization'),

            html.Div(children='''
                Data source: https://www.kaggle.com/stefanoleone992/fifa-20-complete-player-dataset
            ''')
        ], className='row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='graph1',
                    figure=fig1
                )
            ], className='six columns'),

            html.Div([
                dcc.Graph(
                    id='graph2',
                    figure=fig2
                )
            ], className='six columns')
        ], className='row')
    ])
)

if __name__ == '__main__':
    app.run_server(debug=True)