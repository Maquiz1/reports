# Accompanied to the visit
import pandas as pd


df = pd.read_excel('CLIENTS.xlsx')

# df = df['education_level'].value_counts()
# print(df)

df = df[(df['education_level'] == 'Not attended school') | (df['education_level'] == 'Primary') | (
    df['education_level'] == 'Secondary') | (df['education_level'] == 'Certificate') | (df['education_level'] == 'Diploma')
    | (df['education_level'] == 'Undergraduate degree') | (df['education_level'] == 'Postgraduate degree')]

dfp = df[(df['education_level'] == 'Primary')]
dfs = df[(df['education_level'] == 'Secondary')]
dft = df[(df['education_level'] == 'Undergraduate degree') |
         (df['education_level'] == 'Postgraduate degree')]
dfo = df[(df['education_level'] == 'Diploma') | (df['education_level']
                                                 == 'Not attended school') | (df['education_level'] == 'Certificate')]
dfp_i = dfp[(dfp['site_id'] == 2) | (dfp['site_id'] == 4)]
dfs_i = dfs[(dfs['site_id'] == 2) | (dfs['site_id'] == 4)]
dft_i = dft[(dft['site_id'] == 2) | (dft['site_id'] == 4)]
dfo_i = dfo[(dfo['site_id'] == 2) | (dfo['site_id'] == 4)]
dfp_c = dfp[(dfp['site_id'] == 1) | (dfp['site_id'] == 3)]
dfs_c = dfs[(dfs['site_id'] == 1) | (dfs['site_id'] == 3)]
dft_c = dft[(dft['site_id'] == 1) | (dft['site_id'] == 3)]
dfo_c = dfo[(dfo['site_id'] == 1) | (dfo['site_id'] == 3)]



df_T = df.shape[0]
df_P = (df_T * 100) / (df_T)


dfp_T = dfp.shape[0]
dfp_P = (dfp_T * 100) / (df_T)

dfs_T = dfs.shape[0]
dfs_P = (dfs_T * 100) / (df_T)

dft_T = dft.shape[0]
dft_P = (dft_T * 100) / (df_T)

dfo_T = dfo.shape[0]
dfo_P = (dfo_T * 100) / (df_T)


dfp_i_T = dfp_i.shape[0]
dfp_i_P = (dfp_i_T * 100) / (df_T)

dfs_i_T = dfs_i.shape[0]
dfs_i_P = (dfs_i_T * 100) / (df_T)

dft_i_T = dft_i.shape[0]
dft_i_P = (dft_i_T * 100) / (df_T)

dfo_i_T = dfo_i.shape[0]
dfo_i_P = (dfo_i_T * 100) / (df_T)



dfp_c_T = dfp_c.shape[0]
dfp_c_P = (dfp_c_T * 100) / (df_T)

dfs_c_T = dfs_c.shape[0]
dfs_c_P = (dfs_c_T * 100) / (df_T)

dft_c_T = dft_c.shape[0]
dft_c_P = (dft_c_T * 100) / (df_T)

dfo_c_T = dfo_c.shape[0]
dfo_c_P = (dfo_c_T * 100) / (df_T)

# ## OUT PUT

print(df_T)
print(df_P)

print(dfp_T)
print(dfp_P)

print(dfs_T)
print(dfs_P)

print(dft_T)
print(dft_P)

print(dfo_T)
print(dfo_P)

print(dfp_i_T)
print(dfp_i_P)

print(dfs_i_T)
print(dfs_i_P)

print(dft_i_T)
print(dft_i_P)

print(dfo_i_T)
print(dfo_i_P)


print(dfp_c_T)
print(dfp_c_P)

print(dfs_c_T)
print(dfs_c_P)

print(dft_c_T)
print(dft_c_P)

print(dfo_c_T)
print(dfo_c_P)