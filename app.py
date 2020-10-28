import os
import gc
from random import randint
import pandas as pd

import flask
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from src.transformations import transform1, transform2, transform3, transform4, transform6, transform7_8
from src.plot import plot1, plot2, plot3, plot4, plot5, plot6, plot7, plot8, plot9, plot10, plot11

server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server)

app.title = 'FIFA Data Visualization'

dfs = {}
for i in range(15, 21):
    dfs[i] = pd.read_csv('./input/players_' + str(i) + '.csv')

descs = {}
for i in range(1, 12):
    with open('./input/descriptions/desc' + str(i) + '.txt' , 'r') as f:
        descs[i] = f.read()

figs = {}        

figs[1] = plot1(transform1(dfs[20]))
figs[2] = plot2(transform2(dfs[20]))
figs[3] = plot3(transform3(dfs))
figs[4] = plot4(transform4(dfs))
figs[5] = plot5(dfs[20])
figs[6] = plot6(transform6(dfs[20]))

trfs7_8 = transform7_8(dfs[20])

figs[7] = plot7(trfs7_8)
figs[8] = plot8(trfs7_8)
figs[9] = plot9(dfs[20])
figs[10] = plot10(dfs[20])
figs[11] = plot11(dfs[20])

del dfs
gc.collect()

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
github = "https://github.com/alvaro-rodrigues/fifa-infovis"
kaggle = "https://www.kaggle.com/stefanoleone992/fifa-20-complete-player-dataset"
youtube = "https://www.youtube.com/watch?v=1CaibmPOb8A"


layout = [
        dbc.Navbar(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                            dbc.Col(dbc.NavbarBrand("FIFA Data Visualization", className="ml-2")),
                            dbc.Col(dbc.Nav(dbc.NavItem(dbc.NavLink("Code", href=github, target="_blank")), navbar=True)),
                            dbc.Col(dbc.Nav(dbc.NavItem(dbc.NavLink("Data", href=kaggle, target="_blank")), navbar=True)),
                            dbc.Col(dbc.Nav(dbc.NavItem(dbc.NavLink("Video", href=youtube, target="_blank")), navbar=True))
                        ],
                        align="center",
                        no_gutters=True,
                    ),
                    href="#",
                ),
                dbc.NavbarToggler(id="navbar-toggler"),
            ],
            color="dark",
            dark=True,
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='graph1', figure=figs[1]),
                        width=6, lg={'size': 6,  "offset": 0, 'order': 'first'}
                        ),
                dbc.Col(dcc.Graph(id='graph2', figure=figs[2]),
                        width=6, lg={'size': 6,  "offset": 0, 'order': 'last'}
                        )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    children = [
                        dbc.Button(
                            "+Informações",
                            id="collapse-button1",
                            className="mb-3",
                            color="dark",
                        ),
                        dbc.Collapse(
                            dbc.Card(dbc.CardBody(dcc.Markdown(descs[1])), style={"font-size": "16px"}),
                            id="collapse1",
                        )
                    ],
                width=6, lg={'size': 6,  "offset": 0, 'order': 'first'}
                ),
               dbc.Col(
                   children = [
                        dbc.Button(
                            "+Informações",
                            id="collapse-button2",
                            className="mb-3",
                            color="dark",
                        ),
                        dbc.Collapse(
                            dbc.Card(dbc.CardBody(dcc.Markdown(descs[2])), style={"font-size": "16px"}),
                            id="collapse2",
                        )
                    ],
                width=6, lg={'size': 6,  "offset": 0, 'order': 'first'}
                )
            ]
        )
    ]

for i in range(3, 12):

    layout += [
        dbc.Row(dbc.Col(dcc.Graph(id='graph' + str(i), figure=figs[i]),
            width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    children = [
                        dbc.Button(
                            "+Informações",
                            id="collapse-button" + str(i),
                            className="mb-3",
                            color="dark",
                        ),
                        dbc.Collapse(
                            dbc.Card(dbc.CardBody(dcc.Markdown(descs[i])), style={"font-size": "16px"}),
                            id="collapse" + str(i),
                        )
                    ],
                width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                )
            ]
        )
    ]        

app.layout = html.Div(layout)

def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in range(11):
    app.callback(
        Output("collapse" + str(i+1), "is_open"),
        [Input("collapse-button" + str(i+1), "n_clicks")],
        [State("collapse" + str(i+1), "is_open")],
    )(toggle_collapse)

if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)