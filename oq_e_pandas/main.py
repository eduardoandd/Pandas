import pandas as pd

df = pd.read_csv('supermarket_sales.csv')

#FATURAMENTO POR FILIAL
df.groupby('City')[['Total']].sum()

#PORNCETUAL DE PARTICIPAÇÃO NA RECEITA DE CADA TIPO DE PRODUTO
(df.groupby('Product line')['Total'].sum() / df.groupby('Product line')['Total'].sum().sum()).sort_values() * 100

#COMO ESTÁ DISTRIBUIDO O TIPO DE PRODUTO CONSUMIDO POR GENERO
df.groupby(['Gender','Product line'])[['Total']].sum().pivot_table(index='Product line', columns='Gender')

#FATURAMENTO POR MES
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].apply(lambda x: x.month)
df['Year'] = df['Date'].apply(lambda x: x.year)
df.groupby('Month')['Total'].sum()
df.groupby('Year')['Total'].sum() # ANO


#MÉDIA DA AVALIAÇÃO POR CADA FILIAL EM JANEIRO 2019
df[(df['Year'] == 2019) & (df['Month'] == 1)]['Rating'].mean()

# COMO SE DISTRIBUI O GASTO POR TIDO DE CONSUMIDOR EM CADA FILIAL
df.groupby(['City','Customer type'])[['Total']].sum()
