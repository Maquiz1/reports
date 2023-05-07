import pandas as pd


df = pd.read_excel('Retrospective_Data.xlsx')
df = df[['country', 'name', 'id', 'status', 'hospital', 'age', 'sex']]
df = df[df.country == 'Tanzania']
df = df[df.id.str.contains("TB")]

df2 = df[['country', 'name', 'id', 'status', 'hospital', 'age', 'sex']].sort_values('id')

df = df[df.duplicated(subset=['id'], keep=False)].sort_values('id')
print(df2)

df2.to_excel('Retrospective Data Tanzania.xlsx', index=False)