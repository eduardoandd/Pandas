import pandas as pd

dias_contados = 132
date = pd.date_range(start='2023/08/27',periods=dias_contados)

df = pd.DataFrame(range(dias_contados), columns=['numeros'],index=date)

df.index
df.index[1].year
df.index[1].month
#PUXA UM DATA FRAME AONDE O MES DO INDEX É IGUAL A 1
df[df.index.month==1]

import datetime

#PEGA DADOS EM QUE O DATETIME FOI MAIOR Q ESSA DATA
df[df.index > datetime.datetime(2023, 12 , 13)]
