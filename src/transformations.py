import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def transform1(df20):

    df_radar = df20[['short_name', 'overall', 'player_positions', 'pace',
                    'shooting', 'passing', 'dribbling', 'defending', 'physic']]

    df_radar = df_radar.dropna()

    df_radar.loc[:, 'player_positions'] = df_radar['player_positions'].str.split(pat=",")
    df_radar.loc[:, 'player_positions'] = df_radar.player_positions.map(lambda x: x[0])
    df_radar = df_radar.loc[df_radar['player_positions'] != 'GK']

    col = 'player_positions'

    conditions = [(df_radar[col] == 'CB') | (df_radar[col] == 'CDM'),
                (df_radar[col] == 'LB') | (df_radar[col] == 'LWB') | (df_radar[col] == 'RB') | (df_radar[col] == 'RWB'),
                (df_radar[col] == 'CM') | (df_radar[col] == 'LM') | (df_radar[col] == 'RM') | (df_radar[col] == 'CAM'),
                (df_radar[col] == 'LW') | (df_radar[col] == 'RW'),
                (df_radar[col] == 'ST') | (df_radar[col] == 'CF')]

    choices = ['Defender', 'Wing Back', 'Midfielder', 'Wing Forward', 'Forward']
        
    df_radar["position"] = np.select(conditions, choices, default=np.nan)

    df_48_60 = df_radar.loc[df_radar['overall'] < 60]
    df_60_70 = df_radar.loc[(df_radar['overall'] <= 60) & (df_radar['overall'] < 70)]
    df_70_80 = df_radar.loc[(df_radar['overall'] <= 70) & (df_radar['overall'] < 80)]
    df_80_94 = df_radar.loc[df_radar['overall'] >= 80]

    def groupby_pos(df):
        
        df_grouped = df.groupby('position', as_index=False).agg({
            'pace'      : 'median',
            'shooting'  : 'median',
            'passing'   : 'median',
            'dribbling' : 'median',
            'defending' : 'median',
            'physic'    : 'median'
        })

        return df_grouped


    df_lst = [df_48_60, df_60_70, df_70_80, df_80_94]
    df_lst = [df.pipe(groupby_pos) for df in df_lst]

    return df_lst

def transform2(df20):

    df_scatter = df20[['short_name', 'overall', 'club', 'value_eur', 'player_positions']]
    df_scatter = df_scatter.dropna()

    df_scatter.loc[:, 'player_positions'] = df_scatter['player_positions'].str.split(pat=",")
    df_scatter.loc[:, 'player_positions'] = df_scatter.player_positions.map(lambda x: x[0])

    col = 'player_positions'

    conditions = [df_scatter[col] == 'GK',
                (df_scatter[col] == 'CB') | (df_scatter[col] == 'CDM'),
                (df_scatter[col] == 'LB') | (df_scatter[col] == 'LWB') | (df_scatter[col] == 'RB') | (df_scatter[col] == 'RWB'),
                (df_scatter[col] == 'CM') | (df_scatter[col] == 'LM') | (df_scatter[col] == 'RM') | (df_scatter[col] == 'CAM'),
                (df_scatter[col] == 'LW') | (df_scatter[col] == 'RW'),
                (df_scatter[col] == 'ST') | (df_scatter[col] == 'CF')]

    choices = ['Goalkeeper', 'Defender', 'Wing Back', 'Midfielder', 'Wing Forward', 'Forward']
        
    df_scatter["position"] = np.select(conditions, choices, default=np.nan)

    return df_scatter