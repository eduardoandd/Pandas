import pandas as pd

df=pd.read_csv('top250-00-19.csv')

df.groupby(['Position']).sum()
df.groupby(['Position'])['Transfer_fee'].mean().sort_values(ascending=True)
df.groupby(['Position'])['Transfer_fee'].mean().sort_values(ascending=False)
df.groupby('Position')['Age'].mean().sort_values(ascending=False)
df.groupby('Position')['Age'].min().sort_values(ascending=False)

df2 = df[['Name','Position','Age']].copy()
df3 = df[['Transfer_fee','Season']].copy()
df4 = df2.join(df3)

