import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import plotly.express as px

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
    height=900, width=900,
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
        height=900, width=900,
        autosize=False,
        scene=dict(aspectmode="manual", aspectratio=dict(x=1, y=1)),
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        title_text="Value vs. overall of the players of the 9 most valuable teams"
    )

    return fig

def plot3(overs):

    x = [15, 16, 17, 18, 19, 20]

    subplots = {0 : {'row' : 1, 'col' : 1},
                1 : {'row' : 1, 'col' : 2},
                2 : {'row' : 1, 'col' : 3},
                3 : {'row' : 1, 'col' : 4},
                4 : {'row' : 1, 'col' : 5},
                5 : {'row' : 2, 'col' : 1},
                6 : {'row' : 2, 'col' : 2},
                7 : {'row' : 2, 'col' : 3},
                8 : {'row' : 2, 'col' : 4},
                9 : {'row' : 2, 'col' : 5}}

    fig = make_subplots(rows = 2, cols = 5, vertical_spacing= 0.1, subplot_titles = (list(overs.keys())
                                                                                    ))
    for i, key in enumerate(list(overs.keys())):

        fig.add_trace(go.Scatter(
                x = x,
                y= overs[key],
                mode = 'markers+lines',
                line_color= 'rgb(255, 217, 47)',
                name= 'Mahrez',
                showlegend= False),
            row = subplots[i]['row'],
            col = subplots[i]['col']
            )

        fig.add_trace(go.Scatter(
                x = x,
                y= overs['mean'],
                mode = 'markers+lines',
                line_color= 'rgb(179, 179, 179)',
                line_width = 1,
                name= 'Mean',
                showlegend= False),
            row = subplots[i]['row'],
            col = subplots[i]['col']
            )

    fig.update_layout(
        width=1500,
        height=750,
        title = "<b>Overall dos Jogadores Indicados ao Bola de Ouro 2019 a partir do FIFA 15<b>",
        title_font_size = 25,
        title_xanchor = 'left')

    fig.update_yaxes(range=[68, 96])

    return fig

def plot4(pots):

    x = [15, 16, 17, 18, 19, 20]

    subplots = {0 : {'row' : 1, 'col' : 1},
                1 : {'row' : 1, 'col' : 2},
                2 : {'row' : 1, 'col' : 3},
                3 : {'row' : 1, 'col' : 4},
                4 : {'row' : 1, 'col' : 5},
                5 : {'row' : 2, 'col' : 1},
                6 : {'row' : 2, 'col' : 2},
                7 : {'row' : 2, 'col' : 3},
                8 : {'row' : 2, 'col' : 4},
                9 : {'row' : 2, 'col' : 5}}

    fig = make_subplots(rows = 2, cols = 5,vertical_spacing= 0.1, subplot_titles = (list(pots.keys())
                                                                                    ))

    for i, key in enumerate(list(pots.keys())):
    
        fig.add_trace(go.Scatter(
                x = x,
                y= pots[key],
                mode = 'markers+lines',
                line_color= 'rgb(255, 217, 47)',
                name= 'Mahrez',
                showlegend= False),
            row = subplots[i]['row'],
            col = subplots[i]['col']
            )

        fig.add_trace(go.Scatter(
                x = x,
                y= pots[key],
                mode = 'markers+lines',
                line_color= 'rgb(179, 179, 179)',
                line_width = 1,
                name= 'Mean',
                showlegend= False),
            row = subplots[i]['row'],
            col = subplots[i]['col']
            )

    fig.update_layout(
        width=1500,
        height=750,
        title = "<b>Potential dos Jogadores Indicados ao Bola de Ouro 2019 a partir do FIFA 15<b>",
        title_font_size = 25,
        title_xanchor = 'left')

    fig.update_yaxes(range=[72, 96])

    return fig

def plot5(df20):

    table_data = [['Ranking', 'Nome'],
                [1, 'L. Messi'],
                [2, 'V. van Dijk'],
                [3, 'C. Ronaldo'],
                [4, 'S. Mané'],
                [5, 'M. Salah'],
                [6, 'K. Mbappé'],
                [7, 'Alisson'],
                [8, 'R. Lewandowski'],
                [9, 'B. Silva'],
                [10, 'R. Mahrez']]

    fig = ff.create_table(table_data, height_constant=70)

    overx = [df20.loc[154, 'overall'], df20.loc[41, 'overall'], df20.loc[20, 'overall'], df20.loc[13, 'overall'], df20.loc[10, 'overall'],
            df20.loc[9, 'overall'], df20.loc[39, 'overall'], df20.loc[1, 'overall'], df20.loc[7, 'overall'], df20.loc[0, 'overall']]

    overy = ['R. Mahrez',
    'B. Silva',
    'S. Mané',
    'R. Lewandowski',
    'Alisson',
    'K. Mbappé',
    'M. Salah',
    'V. van Dijk',
    'C. Ronaldo',
    'L. Messi']

    overx.sort()

    color = ['rgb(255, 217, 47)', 'rgb(255, 217, 47)', 'rgb(255, 217, 47)', 'rgb(255, 127, 0)', 'rgb(255, 127, 0)', 'rgb(255, 127, 0)', 'rgb(255, 127, 0)', 'rgb(166, 118, 29)', 'rgb(102, 102, 102)', 'goldenrod']

    trace = go.Bar(
        y=overy,
        x=overx,
        name='Overal',
        showlegend= False,
        orientation='h',
        xaxis='x2', yaxis='y2',
        marker=dict(
            color=color)
    )

    fig.add_traces([trace])

    trace1 = go.Scatter(x=['FIFA', 'Bola de Ouro'], y=[1, 1],
                        marker=dict(color='goldenrod'),
                        name='L. Messi',
                        showlegend= False,
                        line_width = 3,
                        xaxis='x3', yaxis='y3')

    trace2 = go.Scatter(x=['FIFA', 'Bola de Ouro'], y=[2, 3],
                        marker=dict(color='rgb(102, 102, 102)'),
                        name='C. Ronaldo',
                        showlegend= False,
                        line_width = 3,
                        xaxis='x3', yaxis='y3')

    trace3 = go.Scatter(x=['FIFA', 'Bola de Ouro'], y=[3, 2],
                        marker=dict(color='rgb(166, 118, 29)'),
                        name='V. van Dijk',
                        showlegend= False,
                        line_width = 3,
                        xaxis='x3', yaxis='y3')

    trace4 = go.Scatter(x=['FIFA', 'Bola de Ouro'], y=[4, 5],
                        marker=dict(color='rgb(255, 127, 0)'),
                        name='M. Salah',
                        showlegend= False,
                        line_width = 3,
                        xaxis='x3', yaxis='y3')

    trace5 = go.Scatter(x=['FIFA', 'Bola de Ouro'], y=[5, 6],
                        marker=dict(color='rgb(255, 127, 0)'),
                        name='K. Mbappé',
                        showlegend= False,
                        line_width = 3,
                        xaxis='x3', yaxis='y3')

    trace6 = go.Scatter(x=['FIFA', 'Bola de Ouro'], y=[6, 7],
                        marker=dict(color='rgb(255, 127, 0)'),
                        name='Alisson',
                        showlegend= False,
                        line_width = 3,
                        xaxis='x3', yaxis='y3')

    trace7 = go.Scatter(x=['FIFA', 'Bola de Ouro'], y=[7, 8],
                        marker=dict(color='rgb(255, 127, 0)'),
                        name='R. Lewandowski',
                        showlegend= False,
                        line_width = 3,
                        xaxis='x3', yaxis='y3')

    trace8 = go.Scatter(x=['FIFA', 'Bola de Ouro'], y=[8, 4],
                        marker=dict(color='rgb(255, 217, 47)'),
                        name='S. Mané',
                        showlegend= False,
                        line_width = 3,
                        xaxis='x3', yaxis='y3')

    trace9 = go.Scatter(x=['FIFA', 'Bola de Ouro'], y=[9, 9],
                        marker=dict(color='rgb(255, 217, 47)'),
                        name='B. Siilva',
                        showlegend= False,
                        line_width = 3,
                        xaxis='x3', yaxis='y3')

    trace10 = go.Scatter(x=['FIFA', 'Bola de Ouro'], y=[10, 10],
                        marker=dict(color='rgb(255, 217, 47)'),
                        name='R. Mahrez',
                        showlegend= False,
                        line_width = 3,
                        xaxis='x3', yaxis='y3')

    fig.add_traces([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10])


    # initialize xaxis2 and yaxis2
    fig['layout']['xaxis2'] = {}
    fig['layout']['yaxis2'] = {}

    # initialize xaxis3 and yaxis3
    fig['layout']['xaxis3'] = {}
    fig['layout']['yaxis3'] = {}

    # Edit layout for subplots
    fig.layout.xaxis.update({'domain': [0.75, 1]}, {'title': 'Bola de Ouro'})
    fig.layout.xaxis2.update({'domain': [0, 0.4]}, range = [80, 95])
    fig.layout.xaxis3.update({'domain': [0.45, 0.7]})

    fig.layout.yaxis.update({'domain': [0, 1]})
    fig.layout.yaxis2.update({'domain': [0, 0.9]})
    fig.layout.yaxis3.update({'domain': [0, 0.9]})

    # The graph's yaxis MUST BE anchored to the graph's xaxis
    fig.layout.yaxis2.update({'anchor': 'x2'})
    fig.layout.yaxis2.update({'title': 'Jogador'})

    # The graph's yaxis MUST BE anchored to the graph's xaxis
    fig.layout.yaxis3.update({'anchor': 'x3'}, autorange = 'reversed')
    fig.layout.yaxis3.update({'title': 'Ranking'})

    # Update the margins to add a title and see graph x-labels.
    fig.layout.margin.update({'t':100, 'b':50})
    fig.layout.update({'title': '<b>FIFA 20 x Bola de Ouro 2019<b>'}, title_font_size = 35, width=1400,
        height=700 )

    return fig

def plot6(corr_matrix):

    fig = ff.create_annotated_heatmap(z=np.asmatrix(corr_matrix).tolist(),
                                      x=list(corr_matrix.columns),
                                      y=list(corr_matrix.columns),
                                      colorscale='Viridis')

    return fig

def plot7(principalDf):

    color_blind = ['#377EB8', '#FF7F00', '#4DAF4A','#F781BF', '#A65628', 
                   '#984EA3','#999999', '#f2bdd8', '#DEDE00', "#E69F00",
                   "#56B4E9", "#009E73", "#d296f2", "#000000",  "#CC79A7"]
    
    fig = px.scatter_3d(principalDf, x='Componente Principal I', y='Componente Principal II', z='Componente Principal III' ,size_max=14,
                        color="position", color_discrete_sequence=color_blind, hover_name="short_name")
                        
    return fig

def plot8(principalDf):

    color_blind = ['#377EB8', '#FF7F00', '#4DAF4A','#F781BF', '#A65628', 
                   '#984EA3','#999999', '#f2bdd8', '#DEDE00', "#E69F00",
                   "#56B4E9", "#009E73", "#d296f2", "#000000",  "#CC79A7"]
    
    fig = px.scatter(principalDf , x='Componente Principal I', y='Componente Principal II',
                     color= "position", color_discrete_sequence=color_blind,hover_name="short_name")
                        
    return fig
