import pandas as pd

df = pd.read_csv('pl_2020.csv')
df.to_excel('pl_2020_index.xlsx', index=True)

df = pd.read_excel('pl_2020_index.xlsx')

df.groupby('Club')['Age'].mean().sort_values(ascending=True)
df.groupby('Position')['Age'].mean()
df.groupby('Nationality')['Nationality'].value_counts().sort_values(ascending=False)

jogadores_egipicios=df[df['Nationality']=='Egypt']
jogadores_egipicios[['Name', 'Appearances']]

#TIPO DE DADO DE CADA COLUNA
df.info()

#QUANTIDADE DE MEMÓRIA USADA POR COLUNA
df.memory_usage()

#VAI RETORNAR APENAS UM VALOR DE CADA DA COLUNA SELECIONADA
df['Nationality'].unique()

#MOSTRA O TOTAL DE NACIONALIDADE EXSTENTES
df['Nationality'].nunique()

df['Nationality'].value_counts()
df['Nationality'].value_counts().index

#APLICANDO UMA FUNÇÃO A IDADE
def calc(x):
    return x*2

df['Age'].apply(calc)
df['Age'].apply(lambda x: x*2) 

df.groupby('Nationality')['Nationality'].value_counts().max()
df[['Name','Age']].min()
df[['Name','Age']].max()
df.groupby('Name')['Big chances created'].mean().sort_values(ascending=False)

def definicao(x):
    if x >= 3:
        return 'Agressivo'
    elif x < 3 and x > 0:
        return 'penalizado'
    else:
        return 'Manso'
df['definicao'] = df['Red cards'].map(definicao)
df['definicao'].value_counts()
df[df['Red cards'] >= 1]
