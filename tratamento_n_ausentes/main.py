import pandas as pd
import numpy as np

dict_df = {
    'A': [1,2,3],
    'B': [np.nan,10,12],
    'C':[np.nan,11,20],
    'D':[1,11,20],
}

df=pd.DataFrame(dict_df)

#DROPA OS INDICES COM VALORES NULOS
df.dropna()

#DROPA AS COLUNAS COM VALORES NULOS
df.dropna(axis=1)

#??
df.dropna(axis=0, thresh=2)
df.dropna(axis=1, thresh=3)

#PREENCHE OS VALORES NULOS COM ALGO DESEJADO
df.fillna('Nulo')
df.fillna(value='Média: ' + str(df['A'].mean()))

#PREENCHE OS VALORES NULOS COM O VALOR QUE ESTÁ ACIMA
df.ffill()
#PREENCHE OS VALORES NULOS COM OS VALORES QUE ESTÁ ABAIXO
df.bfill()





