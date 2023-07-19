import pandas as pd

df = pd.read_excel('/home/maquiz/Documents/EAPOVL/_2023_07_02/CLIENTS.xlsx')


# df = df.columns
# print(df)
# df = df[df.recent_vl < 50]

df = df[['study_id', 'age', 'gender', 'marital_status',
         'education_level', 'occupation', 'site_id', 'recent_vl', 'recent_vl_date', 'vl', 'vl_date']]

df = df[df.vl.str.contains('', na=False, regex=True) == True] 
# df = df[df.recent_vl.isnull()] 


print(df)

