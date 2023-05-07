# Parental status
import pandas as pd


df = pd.read_excel('~/Documents/EAPOCVL/_2023_05_07/CLIENTS_VARIABLE.xlsx')
# df = df.columns
# print(df)

# df = df['redcap_data_access_group'].value_counts()
# df = df['what_is_the_life_status_of'].value_counts()
# print(df)

df_T = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'sinza_hospital')]


df_L = df_T[(df_T['what_is_the_life_status_of'] == 1) | (df_T['what_is_the_life_status_of'] == 2) | (
    df_T['what_is_the_life_status_of'] == 3) | (df_T['what_is_the_life_status_of'] == 4)]


df1 = df_L[(df_L['what_is_the_life_status_of'] == 1)]
df2 = df_L[(df_L['what_is_the_life_status_of'] == 2)]
df3 = df_L[(df_L['what_is_the_life_status_of'] == 3)]
df4 = df_L[(df_L['what_is_the_life_status_of'] == 4)]


df1_i = df1[(df1['redcap_data_access_group'] == 'mwananyamala_hospi') | (df1['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df2_i = df2[(df2['redcap_data_access_group'] == 'mwananyamala_hospi') | (df2['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df3_i = df3[(df3['redcap_data_access_group'] == 'mwananyamala_hospi') | (df3['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df4_i = df4[(df4['redcap_data_access_group'] == 'mwananyamala_hospi') | (df4['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]

df1_c = df1[(df1['redcap_data_access_group'] == 'amana_hospital') | (df1['redcap_data_access_group'] == 'sinza_hospital')]
df2_c = df2[(df2['redcap_data_access_group'] == 'amana_hospital') | (df2['redcap_data_access_group'] == 'sinza_hospital')]
df3_c = df3[(df3['redcap_data_access_group'] == 'amana_hospital') | (df3['redcap_data_access_group'] == 'sinza_hospital')]
df4_c = df4[(df4['redcap_data_access_group'] == 'amana_hospital') | (df4['redcap_data_access_group'] == 'sinza_hospital')]



df_T = df_T.shape[0]
df_L = df_L.shape[0]
df_P = (df_L * 100) / (df_L)


df1_T = df1.shape[0]
df1_P = (df1_T * 100) / (df_T)

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

print(df_L)
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
