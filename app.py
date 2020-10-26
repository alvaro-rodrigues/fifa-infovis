import os
import gc
from random import randint
import pandas as pd

import flask
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from src.transformations import transform1, transform2, transform3, transform4, transform6, transform7_8
from src.plot import plot1, plot2, plot3, plot4, plot5, plot6, plot7, plot8, plot9, plot10, plot11

server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server)

app.title = 'FIFA Data Visualization'

dfs = {}
for i in range(15, 21):
    dfs[i] = pd.read_csv('./input/players_' + str(i) + '.csv')

fig1 = plot1(transform1(dfs[20]))
fig2 = plot2(transform2(dfs[20]))
fig3 = plot3(transform3(dfs))
fig4 = plot4(transform4(dfs))
fig5 = plot5(dfs[20])
fig6 = plot6(transform6(dfs[20]))

trfs7_8 = transform7_8(dfs[20])

fig7 = plot7(trfs7_8)
fig8 = plot8(trfs7_8)
fig9 = plot9(dfs[20])
fig10 = plot10(dfs[20])
fig11 = plot11(dfs[20])

del dfs
gc.collect()

app.layout = html.Div([
        dbc.Row(dbc.Col(html.H3("FIFA Data Visualization"),
                        width={'size': 6, 'offset': 0},
                        ),
                ),
        dbc.Row(dbc.Col(html.Div(
                            children = [
                                html.A("Data source", href='https://www.kaggle.com/stefanoleone992/fifa-20-complete-player-dataset', target="_blank"),
                                html.A("    Code", href='https://github.com/alvaro-rodrigues/fifa-infovis', target="_blank")
                                ]
                            )
                        )
                ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='graph1', figure=fig1),
                        width=6, lg={'size': 6,  "offset": 0, 'order': 'first'}
                        ),
                dbc.Col(dcc.Graph(id='graph2', figure=fig2),
                        width=6, lg={'size': 6,  "offset": 0, 'order': 'last'}
                        )
            ]
        ),
        dbc.Row(dbc.Col(dcc.Graph(id='graph3', figure=fig3),
                        width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                        )
                ),
        dbc.Row(dbc.Col(dcc.Graph(id='graph4', figure=fig4),
                        width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                        )
                ),
        dbc.Row(dbc.Col(dcc.Graph(id='graph5', figure=fig5),
                        width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                        )
                ),
        dbc.Row(dbc.Col(dcc.Graph(id='graph6', figure=fig6),
                        width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                        )
                ),
        dbc.Row(dbc.Col(dcc.Graph(id='graph7', figure=fig7),
                        width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                        )
                ),
        dbc.Row(dbc.Col(dcc.Graph(id='graph8', figure=fig8),
                        width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                        )
                ),
        dbc.Row(dbc.Col(dcc.Graph(id='graph9', figure=fig9),
                        width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                        )
                ),
        dbc.Row(dbc.Col(dcc.Graph(id='graph10', figure=fig10),
                        width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                        )
                ),
        dbc.Row(dbc.Col(dcc.Graph(id='graph11', figure=fig11),
                        width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                        )
                )                                                                                                            
])

if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)