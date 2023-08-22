import pandas as pd
import numpy as np

df = pd.read_csv('top250-00-19.csv')

labels = ['a','b','c']
minha_lista=[10,8,20]
#minha_lista_2=[10,8,'a']
arr =np.array([10,20,30])
d = {'a':1,'b':2,'c':3,'d':4}

# SERIES SÃO COLUNAS DA TABELA.
pd.Series(labels)
pd.Series(minha_lista)
pd.Series(arr)

pd.Series(data=labels,index=minha_lista)

#LABEL CIADA POR DICIONARO
pd.Series(d)

ser1=pd.Series(index=['BRASIL','EUA','ALEMANHA','ARGENTINA'],data=['A','B','C','D'])
ser1['BRASIL']


ser2=pd.Series(index=['BRASIL','ARGENTINA','EUA','ALEMANHA'],data=['A','B','C','D'])
ser1+ser2

