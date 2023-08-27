import pandas as pd
import html5lib
#df = pd.read_excel('TESTE.xlsx')
dfcsv= pd.read_csv('top250-00-19.csv')

# CONVERTENDO UM CSV PARA EXCEL
export_excel = dfcsv.to_excel('teste_expor.xlsx')

#LENDO UM ARQUIVO EXCEL CONVERTIDO CSV -> EXCEL
df_excel = pd.read_excel('teste_expor.xlsx')

#LENDO ARQUIVO HTML
df_html=pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
df_html[0]
