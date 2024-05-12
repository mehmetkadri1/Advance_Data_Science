'''''import pandas
csv_path='file1.csv'
df=pandas.read_csv(csv_path )'''''
#pandas opensources data manipulation and data analysis libriary for python programming libriary
#pandas offers two primary data structures DataFrame and Series
import pandas as pd
import numpy as np
filename="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"
df=pd.read_csv(filename)
df.head()
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'
df=pd.read_excel(xlsx_path)
df.head()
x=np.array([[1,0],[0,1]])
y=np.array([[2,5],[6,3]])
a=x*y
print(a)
