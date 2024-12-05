#Creo un ETL para conectar mi archivo csv a PostgreSQL
import pandas as pd    #
import psycopg2

df1 = pd.read_csv('C:/Mis_Archivos/Education/GastoPublico_PIB/Gastopublico_PIB.csv') 
df2 = pd.read_csv('C:/Mis_Archivos/Education/GastoPublico_Presupuesto/Gastopublico_presupuesto.csv')

conn = psycopg2.connect(
    host="localhost",
    database="Educación",
    user="*****",
    password="******"
)
cursor = conn.cursor()

#Creo la primera tabla
cursor.execute("""                                     
CREATE TABLE IF NOT EXISTS public_spending (
    entity VARCHAR(100),
    code VARCHAR(10),
    year INTEGER,
    public_spending_pib NUMERIC
);
""")
#Creo la segunda tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS education_expenditure (
    entity VARCHAR(100),
    code VARCHAR(10),
    year INTEGER,
    government_avgexpenditure NUMERIC
);
""")
    #Importo los datos
for _, row in df1.iterrows():
    cursor.execute("""
    INSERT INTO public_spending (entity, code, year, public_spending_pib)
    VALUES (%s, %s, %s, %s)
    """, (row['entity'], row['code'], row['year'], row['public_spending_pib']))

for _, row in df2.iterrows():
    cursor.execute("""
    INSERT INTO education_expenditure (entity, code, year, government_avgexpenditure)
    VALUES (%s, %s, %s, %s)
    """, (row['entity'], row['code'], row['year'], row['government_avgexpenditure']))
#Cierro la conexion
conn.commit()
cursor.close()
conn.close()
