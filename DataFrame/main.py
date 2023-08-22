from numpy.random import rand
import pandas as pd

#GERANDO NÚMEROS ALEATÓRIOS DE 5 LINHAS E 4 COLUNAS
pd.DataFrame(rand(5,4), index='A B C D E'.split(), columns= '1 2 3 4'.split())

df = pd.read_csv('top250-00-19.csv')

#CRIANDO NOVA COLUNA APARTIR DE UMA JA EXISTENTE
league_and_team=df['League and Team'] = df['League_to'] + ' | ' + df['Team_to']

#DROPANDO COLUNA
df.drop('League and Team', axis=1)

#DROPANDO O INDICE. INPLACE DEFINI QUE ESSA ALTERAÇÃO É PERMANENTE
df.drop(4, axis=0, inplace=True)


#PEGA A LINHA 0 E 3 DA COLUNA AGE E NAME
df.loc[[0,3],['Age','Name']]

#PEGA A LINHA 0 A 5 DA COLUNA 3 A 8
df.iloc[0:5,3:8]
