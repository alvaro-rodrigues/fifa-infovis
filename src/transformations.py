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

def transform3(df15, df16, df17, df18, df19, df20):

    short15 = df15.loc[[0, 1, 12, 689, 1194, 3318, 3452], ['short_name', 'overall', 'potential']]
    medias15 = [short15['overall'].mean(), short15['potential'].mean()]
    short16 = df16.loc[[0, 1, 14, 271, 575, 398, 1712], ['short_name', 'overall', 'potential']]
    medias16 = [short16['overall'].mean(), short16['potential'].mean()]
    short17 = df17.loc[[1, 0, 9, 282, 549, 275, 63, 396, 3899, 560], ['short_name', 'overall', 'potential']]
    medias17 = [short17['overall'].mean(), short17['potential'].mean()]
    short18 = df18.loc[[1, 0, 5, 148, 103, 92, 157, 417, 126, 146], ['short_name', 'overall', 'potential']]
    medias18 = [short18['overall'].mean(), short18['potential'].mean()]
    short19 = df19.loc[[1, 0, 14, 31, 62, 113, 110, 81, 41, 89], ['short_name', 'overall', 'potential']]
    medias19 = [short19['overall'].mean(), short19['potential'].mean()]
    short20 = df20.loc[[0, 1, 20, 9, 39, 41, 154, 13, 10, 7], ['short_name', 'overall', 'potential']]
    medias20 = [short20['overall'].mean(), short20['potential'].mean()]

    over_messi = [df15.loc[0, 'overall'], df16.loc[0, 'overall'], df17.loc[1, 'overall'], df18.loc[1, 'overall'], df19.loc[1, 'overall'], df20.loc[0, 'overall']]
    over_cris = [df15.loc[1, 'overall'], df16.loc[1, 'overall'], df17.loc[0, 'overall'], df18.loc[0, 'overall'], df19.loc[0, 'overall'], df20.loc[1, 'overall']]
    over_lewa = [df15.loc[12, 'overall'], df16.loc[14, 'overall'], df17.loc[9, 'overall'], df18.loc[5, 'overall'], df19.loc[14, 'overall'], df20.loc[20, 'overall']]
    over_salah = [df15.loc[689, 'overall'], df16.loc[271, 'overall'], df17.loc[282, 'overall'], df18.loc[148, 'overall'], df19.loc[31, 'overall'], df20.loc[9, 'overall']]
    over_mane = [df15.loc[1194, 'overall'], df16.loc[575, 'overall'], df17.loc[549, 'overall'], df18.loc[103, 'overall'], df19.loc[62, 'overall'], df20.loc[39, 'overall']]
    over_ber = [df15.loc[3318, 'overall'], df16.loc[398, 'overall'], df17.loc[275, 'overall'], df18.loc[92, 'overall'], df19.loc[113, 'overall'], df20.loc[41, 'overall']]
    over_mar = [df15.loc[3452, 'overall'], df16.loc[1712, 'overall'], df17.loc[63, 'overall'], df18.loc[157, 'overall'], df19.loc[110, 'overall'], df20.loc[154, 'overall']]
    over_ali = [None, None, df17.loc[396, 'overall'], df18.loc[417, 'overall'], df19.loc[81, 'overall'], df20.loc[13, 'overall']]
    over_mba = [None, None, df17.loc[3899, 'overall'], df18.loc[126, 'overall'], df19.loc[41, 'overall'], df20.loc[10, 'overall']]
    over_dijk = [None, None, df17.loc[560, 'overall'], df18.loc[146, 'overall'], df19.loc[89, 'overall'], df20.loc[7, 'overall']]

    over_mean = [medias15[0], medias16[0], medias17[0], medias18[0], medias19[0], medias20[0]]
    overs = [over_messi, over_cris, over_lewa, over_salah, over_mane, over_ber, over_mar, over_ali, over_mba, over_dijk, over_mean]

    return overs

def transform4(df15, df16, df17, df18, df19, df20):

    short15 = df15.loc[[0, 1, 12, 689, 1194, 3318, 3452], ['short_name', 'overall', 'potential']]
    medias15 = [short15['overall'].mean(), short15['potential'].mean()]
    short16 = df16.loc[[0, 1, 14, 271, 575, 398, 1712], ['short_name', 'overall', 'potential']]
    medias16 = [short16['overall'].mean(), short16['potential'].mean()]
    short17 = df17.loc[[1, 0, 9, 282, 549, 275, 63, 396, 3899, 560], ['short_name', 'overall', 'potential']]
    medias17 = [short17['overall'].mean(), short17['potential'].mean()]
    short18 = df18.loc[[1, 0, 5, 148, 103, 92, 157, 417, 126, 146], ['short_name', 'overall', 'potential']]
    medias18 = [short18['overall'].mean(), short18['potential'].mean()]
    short19 = df19.loc[[1, 0, 14, 31, 62, 113, 110, 81, 41, 89], ['short_name', 'overall', 'potential']]
    medias19 = [short19['overall'].mean(), short19['potential'].mean()]
    short20 = df20.loc[[0, 1, 20, 9, 39, 41, 154, 13, 10, 7], ['short_name', 'overall', 'potential']]
    medias20 = [short20['overall'].mean(), short20['potential'].mean()]

    pot_messi = [df15.loc[0, 'potential'], df16.loc[0, 'potential'], df17.loc[1, 'potential'], df18.loc[1, 'potential'], df19.loc[1, 'potential'], df20.loc[0, 'potential']]
    pot_cris = [df15.loc[1, 'potential'], df16.loc[1, 'potential'], df17.loc[0, 'potential'], df18.loc[0, 'potential'], df19.loc[0, 'potential'], df20.loc[1, 'potential']]
    pot_lewa = [df15.loc[12, 'potential'], df16.loc[14, 'potential'], df17.loc[9, 'potential'], df18.loc[5, 'potential'], df19.loc[14, 'potential'], df20.loc[20, 'potential']]
    pot_salah = [df15.loc[689, 'potential'], df16.loc[271, 'potential'], df17.loc[282, 'potential'], df18.loc[148, 'potential'], df19.loc[31, 'potential'], df20.loc[9, 'potential']]
    pot_mane = [df15.loc[1194, 'potential'], df16.loc[575, 'potential'], df17.loc[549, 'potential'], df18.loc[103, 'potential'], df19.loc[62, 'potential'], df20.loc[39, 'potential']]
    pot_ber = [df15.loc[3318, 'potential'], df16.loc[398, 'potential'], df17.loc[275, 'potential'], df18.loc[92, 'potential'], df19.loc[113, 'potential'], df20.loc[41, 'potential']]
    pot_mar = [df15.loc[3452, 'potential'], df16.loc[1712, 'potential'], df17.loc[63, 'potential'], df18.loc[157, 'potential'], df19.loc[110, 'potential'], df20.loc[154, 'potential']]
    pot_ali = [None, None, df17.loc[396, 'potential'], df18.loc[417, 'potential'], df19.loc[81, 'potential'], df20.loc[13, 'potential']]
    pot_mba = [None, None, df17.loc[3899, 'potential'], df18.loc[126, 'potential'], df19.loc[41, 'potential'], df20.loc[10, 'potential']]
    pot_dijk = [None, None, df17.loc[560, 'potential'], df18.loc[146, 'potential'], df19.loc[89, 'potential'], df20.loc[7, 'potential']]

    pot_mean = [medias15[1], medias16[1], medias17[1], medias18[1], medias19[1], medias20[1]]
    pots = [pot_messi, pot_cris, pot_lewa, pot_salah, pot_mane, pot_ber, pot_mar, pot_ali, pot_mba, pot_dijk, pot_mean]

    return pots