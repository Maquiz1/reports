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
df_P = (df_L * 100) / (df_T)


df1_T = df1.shape[0]
df1_P = (df1_T * 100) / (df_L)

df2_T = df2.shape[0]
df2_P = (df2_T * 100) / (df_L)

df3_T = df3.shape[0]
df3_P = (df3_T * 100) / (df_L)

df4_T = df4.shape[0]
df4_P = (df4_T * 100) / (df_L)


df1_i_T = df1_i.shape[0]
df1_i_P = (df1_i_T * 100) / (df1_T)

df2_i_T = df2_i.shape[0]
df2_i_P = (df2_i_T * 100) / (df2_T)

df3_i_T = df3_i.shape[0]
df3_i_P = (df3_i_T * 100) / (df3_T)

df4_i_T = df4_i.shape[0]
df4_i_P = (df4_i_T * 100) / (df4_T)


df1_c_T = df1_c.shape[0]
df1_c_P = (df1_c_T * 100) / (df1_T)

df2_c_T = df2_c.shape[0]
df2_c_P = (df2_c_T * 100) / (df2_T)

df3_c_T = df3_c.shape[0]
df3_c_P = (df3_c_T * 100) / (df3_T)

df4_c_T = df4_c.shape[0]
df4_c_P = (df4_c_T * 100) / (df4_T)

# ## OUT PUT

print(df_L)
print(df_T)
print(df_P)

print(df1_T)
print(df1_P)

print(df2_T)
print(df2_P)

print(df3_T)
print(df3_P)

print(df4_T)
print(df4_P)

print(df1_i_T)
print(df1_i_P)

print(df2_i_T)
print(df2_i_P)

print(df3_i_T)
print(df3_i_P)

print(df4_i_T)
print(df4_i_P)


print(df1_c_T)
print(df1_c_P)

print(df2_c_T)
print(df2_c_P)

print(df3_c_T)
print(df3_c_P)

print(df4_c_T)
print(df4_c_P)
