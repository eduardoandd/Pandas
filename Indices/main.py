import pandas as pd
import numpy as np
from numpy.random import randn 

df=pd.read_csv('top250-00-19.csv')

#RETORNA LISTA DE INDEX E COLUNAS
df.index
df.columns

#CRIA UMA COLUNA CHAMADA INDEX E CRIA NOVOS INDEX
df.reset_index(inplace=True)

#DEFINI UMA COLUNA COMO O NOVO INDEX
df.set_index('index', inplace=True)

#CRIANDO UMA NOVA COLUNA E ADICIONANDO A LETRA L
df['new index'] = [f'L{i}' for i in range(len(df))] 

#RESETANDO O INDEX PARA NÃO PERDER A INFORMAÇÃO E SETANDO O NOVO.
df.reset_index().set_index('new index')


#============== INDICES MULTINÍVEIS ==============#

outisde= ['G1','G1','G1','G2','G2','G2']
inside= [1,2,3, 1,2,3]

lista = list(zip(outisde,inside))

index = pd.MultiIndex.from_tuples(lista)

df_index = pd.DataFrame(np.random.randn(6,2), index=index, columns=['A','B'])


df_index.loc[['G1','G2']]
df_index.loc['G1'].loc[1]

#DEFINE NOME PARA CADA INDEX
df_index.index.names = ['Grupos', 'Numeros']

# PEGA TODOS OS INDICES 1
df_index.xs(1, level='Numeros')








