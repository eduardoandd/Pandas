import pandas as pd

df = pd.read_csv('top250-00-19.csv')



# LOC TRABALHA COM VALORES EM STRING E NUMERICOS
df.loc[0,'Team_from']
df.loc[1,'Team_from']
df.loc[[0,15,20], 'Team_from']
df.loc[[15,20],['Team_from','Team_to']]
df.loc[[100,110],'Team_from']

# ILOC TRABALHA COM VALORES APENAS NUMERICOS
df.iloc[10,[0,3,5,9]]
df.iloc[12,[0,1,3,5,7]]
df.iloc[0,[2,1]]

# EXPRESSÃO CONDICIONAIS
df['Age'] > 30
df[df['Age'] > 30]
df[(df['Age'] > 18) & (df['Transfer_fee'] > 100000000)]
df[(df.loc[0:,'Age'] > 30) & (df.iloc[0:,4]=='Serie A')]