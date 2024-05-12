import pandas as pd
import sqlite3
data = pd.read_csv('./menu.csv')
conn = sqlite3.connect('McDonalds.db')
data.to_sql('MCDONALDS_NUTRITION', conn)
df = pd.read_sql('SELECT * FROM MCDONALDS_NUTRITION', conn)
print(df)
df.describe(include='all') 