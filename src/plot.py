import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot1(df_lst):

    theta = ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'pace']
    positions  = ['Defender', 'Forward', 'Midfielder', 'Wing Back', 'Wing Forward']

    subplots = {0 : {'row' : 1, 'col' : 1},
                1 : {'row' : 1, 'col' : 2},
                2 : {'row' : 2, 'col' : 1},
                3 : {'row' : 2, 'col' : 2}}

    showlegend = False

    colors = ['#636EFA', '#EF553B', '#00CC96', '#FECB52', '#19D3F3']

    fig = make_subplots(rows=2, cols=2,
                        specs=[[{"type": "scatterpolar"}, {"type": "scatterpolar"}],
                            [{"type": "scatterpolar"}, {"type": "scatterpolar"}]],
                        subplot_titles=("Overall [48,59]", "Overall [60, 69]",
                                        "Overall [70, 79]", "Overall [80, 94]"),
                        vertical_spacing=0.05, horizontal_spacing=0.17)

    for i, df in enumerate(df_lst):
        
        if i == 0:
            showlegend = True
        else:
            showlegend = False
        
        for j, pos in enumerate(positions):
            
            fig.add_trace(
                go.Scatterpolar(
                r = df[theta].iloc[j].to_list() + [df[theta].iloc[j].to_list()[0]],
                theta = theta,
                mode = 'lines',
                name = pos,
                showlegend = showlegend,
                legendgroup = pos,
                line=dict(
                    color=colors[j])
                ),
            row = subplots[i]['row'],
            col = subplots[i]['col']
            )
            
    fig.update_layout(
    height=950, width=950,
    title_text="Median of attributes by player position",
    polar1=dict(
        radialaxis=dict(
        visible=True,
        range=[25, 90]
        )
    ),
    polar2=dict(
        radialaxis=dict(
        visible=True,
        range=[25, 90]
        )
    ),
    polar3=dict(
        radialaxis=dict(
        visible=True,
        range=[25, 90]
        )
    ),
    polar4=dict(
        radialaxis=dict(
        visible=True,
        range=[25, 90]
        )
    )
    )

    fig.update_yaxes(automargin=True)

    return fig

def plot2(df_scatter):

    clubs = df_scatter.groupby('club', as_index=False)['value_eur'].sum() \
        .sort_values('value_eur', ascending=False).iloc[:9]['club'].to_list()

    positions  = ['Goalkeeper', 'Defender', 'Forward', 'Midfielder', 'Wing Back', 'Wing Forward']

    subplots = {0 : {'row' : 1, 'col' : 1},
                1 : {'row' : 1, 'col' : 2},
                2 : {'row' : 1, 'col' : 3},
                3 : {'row' : 2, 'col' : 1},
                4 : {'row' : 2, 'col' : 2},
                5 : {'row' : 2, 'col' : 3},
                6 : {'row' : 3, 'col' : 1},
                7 : {'row' : 3, 'col' : 2},
                8 : {'row' : 3, 'col' : 3}}

    showlegend = False

    colors = ['#FF6692', '#636EFA', '#EF553B', '#00CC96', '#FECB52', '#19D3F3']

    fig = make_subplots(rows=3, cols=3,
                        specs=[[{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}],
                            [{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}],
                            [{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}]],
                        subplot_titles=clubs,
                        shared_xaxes=True,
                        shared_yaxes=True,
                        vertical_spacing=0.055, horizontal_spacing=0.035)

    for i, club in enumerate(clubs):
        
        if i == 0:
            showlegend = True
        else:
            showlegend = False
        
        for j, pos in enumerate(positions):
            
            df = df_scatter.loc[(df_scatter['club'] == club) & (df_scatter['position'] == pos)]
            
            fig.add_trace(
                go.Scatter(
                x = df['overall'], y = df['value_eur'],
                text = df['short_name'],
                mode = 'markers',
                name = pos,
                showlegend = showlegend,
                legendgroup = pos,
                marker_color = colors[j]
                ),
            row = subplots[i]['row'],
            col = subplots[i]['col']
            )
            
    for i in range(9):
        
        if i == 6 or i == 7 or i == 8:
            fig.update_xaxes(title_text='Overall', range=[53, 97],
                            row=subplots[i]['row'], col=subplots[i]['col']) 
        else:
            fig.update_xaxes(range=[53, 97],
                            row=subplots[i]['row'], col=subplots[i]['col'])
            
        if i == 0 or i == 3 or i == 6:
            fig.update_yaxes(title_text='Value', range=[-3000000, 110000000],
                            row=subplots[i]['row'], col=subplots[i]['col'])
        else:    
            fig.update_yaxes(range=[-3000000, 110000000],
                            row=subplots[i]['row'], col=subplots[i]['col'])
            
    fig.update_layout(
        height=940, width=970,
        autosize=False,
        scene=dict(aspectmode="manual", aspectratio=dict(x=1, y=1)),
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        title_text="Value vs. overall of the players of the 9 most valuable teams"
    )

    return fig