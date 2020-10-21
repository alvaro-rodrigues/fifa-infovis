import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

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

def transform3(dfs):

    players = ['R. Mahrez',
               'B. Silva',
               'R. Lewandowski',
               'Alisson',
               'K. Mbappé',
               'M. Salah',
               'S. Mané',
               'C. Ronaldo',
               'V. van Dijk',
               'L. Messi',
               'Bernardo Silva',
               'K. Mbappe Lottin']
    
    medias = {}
    overs = {key:[] for key in players[:-2]}

    for i in range(15, 21):

        short = dfs[i].loc[dfs[i]['short_name'].isin(players), ['short_name', 'overall', 'potential']]
        medias[i] = [short['overall'].mean(), short['potential'].mean()]

        for key in overs:

            if key == 'K. Mbappé':

                if i == 15 or i == 16:
                    overs[key] += [None]
                else:
                    overs[key] += [short.loc[(short['short_name'] == key) | 
                                             (short['short_name'] == 'K. Mbappe Lottin'), 'overall'].values[0]]

            elif key == 'Alisson':
                
                if i == 15 or i == 16:
                    overs[key] += [None]
                else:
                    overs[key] += [short.loc[short['short_name'] == key, 'overall'].values[0]]

            elif key == 'V. van Dijk':
                
                if i == 15 or i == 16:
                    overs[key] += [None]
                else:
                    overs[key] += [short.loc[short['short_name'] == key, 'overall'].values[0]]

            elif key == 'B. Silva':

                overs[key] += [short.loc[(short['short_name'] == key) | 
                                            (short['short_name'] == 'Bernardo Silva'), 'overall'].values[0]]
            else:
                overs[key] += [short.loc[short['short_name'] == key, 'overall'].values[0]]

    overs['mean'] = [medias[key][0] for key in medias]

    return overs

def transform4(dfs):

    players = ['R. Mahrez',
               'B. Silva',
               'R. Lewandowski',
               'Alisson',
               'K. Mbappé',
               'M. Salah',
               'S. Mané',
               'C. Ronaldo',
               'V. van Dijk',
               'L. Messi',
               'Bernardo Silva',
               'K. Mbappe Lottin']
    
    medias = {}
    pots = {key:[] for key in players[:-2]}

    for i in range(15, 21):

        short = dfs[i].loc[dfs[i]['short_name'].isin(players), ['short_name', 'overall', 'potential']]
        medias[i] = [short['overall'].mean(), short['potential'].mean()]

        for key in pots:

            if key == 'K. Mbappé':

                if i == 15 or i == 16:
                    pots[key] += [None]
                else:
                    pots[key] += [short.loc[(short['short_name'] == key) | 
                                            (short['short_name'] == 'K. Mbappe Lottin'), 'potential'].values[0]]

            elif key == 'Alisson':
                
                if i == 15 or i == 16:
                    pots[key] += [None]
                else:
                    pots[key] += [short.loc[short['short_name'] == key, 'potential'].values[0]]

            elif key == 'V. van Dijk':
                
                if i == 15 or i == 16:
                    pots[key] += [None]
                else:
                    pots[key] += [short.loc[short['short_name'] == key, 'potential'].values[0]]

            elif key == 'B. Silva':

                pots[key] += [short.loc[(short['short_name'] == key) | 
                                        (short['short_name'] == 'Bernardo Silva'), 'potential'].values[0]]
            else:
                pots[key] += [short.loc[short['short_name'] == key, 'potential'].values[0]]

    pots['mean'] = [medias[key][1] for key in medias]

    return pots

def transform6(players_20):

    players_20 = players_20.replace(to_replace ='\-[0-9]', value = '', regex = True)
    
    some_val = ["height_cm","weight_kg","overall","potential","value_eur","wage_eur","skill_moves","shooting","passing",
                "dribbling","attacking_volleys","movement_reactions","movement_balance","mentality_aggression","mentality_interceptions",
                "mentality_positioning","mentality_penalties","defending","defending_marking","defending_standing_tackle","defending_sliding_tackle"]

    corr_matrix = players_20[some_val].corr(method= "spearman").round(decimals=2)

    return corr_matrix

def transform7_8(players_20):

    players_20 = players_20.replace(to_replace ='\-[0-9]', value = '', regex = True)

    pca_val = ["height_cm","weight_kg","overall","potential","value_eur","wage_eur","skill_moves","shooting","passing",
               "dribbling","defending","attacking_volleys", "movement_reactions","movement_balance","mentality_aggression",
               "mentality_interceptions","gk_diving","gk_handling","gk_kicking","gk_reflexes","gk_speed","gk_positioning",
               "goalkeeping_diving","goalkeeping_handling","goalkeeping_kicking","goalkeeping_positioning","goalkeeping_reflexes",
               "mentality_positioning","mentality_penalties","defending_marking","defending_standing_tackle","defending_sliding_tackle"]

    pca = PCA(n_components=3, svd_solver='full')
    X = players_20[pca_val]
    X = X.fillna(X.mean())
    X = StandardScaler().fit_transform(X)

    principalComponents = pca.fit_transform( X)
    principalDf = pd.DataFrame(data = principalComponents, columns = ['Componente Principal I','Componente Principal II','Componente Principal III'])

    postions = []

    for position in players_20['player_positions']:
        postions.append(position.split(",")[0])


    principalDf['position'] = postions
    principalDf["short_name"]  = players_20["short_name"] 

    return principalDf