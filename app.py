import os
from random import randint
import pandas as pd

import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src.transformations import transform1, transform2, transform3, transform4
from src.plot import plot1, plot2, plot3, plot4, plot5

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

app.title = 'FIFA Data Visualization'

dfs = {}
for i in range(15, 21):
    dfs[i] = pd.read_csv('./input/players_' + str(i) + '.csv')

fig1 = plot1(transform1(dfs[20]))
fig2 = plot2(transform2(dfs[20]))
fig3 = plot3(transform3(dfs[15], dfs[16], dfs[17], dfs[18], dfs[19], dfs[20]))
fig4 = plot4(transform4(dfs[15], dfs[16], dfs[17], dfs[18], dfs[19], dfs[20]))
fig5 = plot5(dfs[20])

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
        ], className='row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='graph3',
                    figure=fig3
                )
            ])
        ], className='row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='graph4',
                    figure=fig4
                )
            ])
        ], className='row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='graph5',
                    figure=fig5
                )
            ])
        ], className='row')
    ])
)

if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)