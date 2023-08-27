import sqlite3
import pandas as pd

#1 - CRIAR CONEXAO
conn = sqlite3.connect('teste.db')
df = pd.read_csv('pl_2020.csv')

#EXPORTAR DADOS PARA O SQL
df.to_sql('PREMIER_LEAGUE_INFO',conn)

#DEFINI UM PONTEIRO
c = conn.cursor()

c.execute('CREATE TABLE JOGADORES (JOGADOR_ID,NOME,IDADE)')
c.execute('DROP TABLE JOGADORES')
c.execute('CREATE TABLE JOGADORES ([index] INTEGER PRIMARY KEY, [NAME] TEXT, [age]INTEGER,[CLUB]TEXT)')

#INSERT
c.execute(''' INSERT INTO JOGADORES VALUES
          (1,'SAKA',22,'ARSENAL'),
          (2,'HAVERTZ',24,'ARSENAL'),
          (3,'WHITE',25,'ARSENAL')
          
          ''')
#COMMIT É NECESSÁRIO PARA SALVAR AS ALTERAÇÕES
conn.commit()


df_data_2= df.loc[4:,['Name','Age','Club']]

#CASO EXISTA IMPLEMNTAR NOVAMENTE(EXCESSÃO DE PRIMARI KEY)
df_data_2.to_sql('JOGADORES', conn, if_exists='append')

#SELECT
c.execute(''' 
          SELECT Age,Club FROM JOGADORES
          
          ''')
#RETORNA O 1 RESULTADO DO COMANDO ACIMA
c.fetchone()
#RETORNADO TODOS OS RESULTADOS DO COMANDO ACIMA
c.fetchall()
df_all=pd.DataFrame(c.fetchall())

df_all.drop(columns='Age')            
df_all.rename(columns={0:'Age',1:'Clube'}, inplace=True)
df_all.groupby('Clube')['Age'].mean().sort_values(ascending=False)

#LENDO UM COMANDO SQL DIREITO
query = 'SELECT * FROM JOGADORES WHERE AGE < 20'
df_age=pd.read_sql(query, conn, index_col='index')
df_age.groupby('CLUB')['age'].mean().sort_values(ascending=True)

#UPDATE E DELETE
c.execute('UPDATE JOGADORES SET NAME="BUKAYO SAKA" WHERE index=1 ')
conn.commit()