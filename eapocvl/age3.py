# Parental status
import pandas as pd


df = pd.read_excel('~/Documents/EAPOCVL/_2023_05_15/CLIENTS.xlsx')
# df = df.columns
# print(df)

# df = df['redcap_event_name'].value_counts()
# df = df['redcap_data_access_group'].value_counts()
# df = df['what_is_the_life_status_of'].value_counts()
# df = df['redcap_event_name'].value_counts()
# print(df)


df = df[(df['redcap_event_name'] == 'screening_arm_1')]


df_T = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'sinza_hospital')]

df_L = df_T[(df_T['e_1_a_age_in_years'] >= 0) & (df_T['e_1_a_age_in_years'] <= 24)]

df_i_T = df_L[(df_L['redcap_data_access_group'] == 'mwananyamala_hospi') | (df_L['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df_c_T = df_L[(df_L['redcap_data_access_group'] == 'amana_hospital') | (df_L['redcap_data_access_group'] == 'sinza_hospital')]


df_L = df_L['e_1_a_age_in_years']
df_MN = df_L.mean()
df_MN_P = (df_MN * 100) / (df_MN)

df_D = df_L.std()
df_D_P = (df_D * 100) / (df_D)


df_M = df_L.median()
df_M_P = (df_M * 100) / (df_M)

df_R = df_L.max() - df_L.min()
df_R_P = (df_R * 100) / (df_R)

# df.groupby("ChildID").apply(lambda x: x['abdomcirc'].max() - x['abdomcirc'].min())


df_i_T = df_i_T['e_1_a_age_in_years']
df_MN_I = df_i_T.mean()
df_MN_I_P = (df_MN_I * 100) / (df_MN)

df_D_I = df_i_T.std()
df_D_I_P = (df_D_I * 100) / (df_D)


df_i_M = df_i_T.median()
df_i_M_P = (df_i_M * 100) / (df_M)

df_i_R = df_i_T.max() - df_i_T.min()
df_i_R_P = (df_i_R * 100) / (df_R)


df_c_T = df_c_T['e_1_a_age_in_years']
df_MN_C = df_c_T.mean()
df_MN_C_P = (df_MN_C * 100) / (df_MN)

df_D_C = df_c_T.std()
df_D_C_P = (df_D_C * 100) / (df_D)


df_c_M = df_c_T.median()
df_c_M_P = (df_c_M * 100) / (df_M)

df_c_R = df_c_T.max() - df_c_T.min()
df_c_R_P = (df_c_R * 100) / (df_R)



# ## OUT PUT
print(f'')
print(f'"NIMR SITES - TANZANIA"')
print(f'"Parental status"')
print(f'')

print(f'Mean                              : {df_MN}')
print(f'Mean (%)                          : {df_MN_P} %')

print(f'Deviation                         : {df_D}')
print(f'Deviation (%)                     : {df_D_P} %')


print(f'Medium                            : {df_M}')
print(f'Medium (%)                        : {df_M_P} %')

print(f'Range                             : {df_R}')
print(f'Range (%)                         : {df_R_P} %')


print(f'')
print(f'Intervtn')
print(f'')

print(f'Mean                              : {df_MN_I}')
print(f'Mean (%)                          : {df_MN_I_P} %')

print(f'Deviation                         : {df_D_I}')
print(f'Deviation (%)                     : {df_D_I_P} %')


print(f'Medium Intervtn                   : {df_i_M}')
print(f'Medium Intervtn  (%)              : {df_i_M_P} %')

print(f'Range Intervtn                    : {df_i_R}')
print(f'Range Intervtn (%)                : {df_i_R_P} %')



print(f'')
print(f'Control')
print(f'')

print(f'Mean                              : {df_MN_C}')
print(f'Mean Control (%)                  : {df_MN_C_P} %')

print(f'Deviation                         : {df_D_C}')
print(f'Deviation Control (%)             : {df_D_C_P} %')


print(f'Medium Control                    : {df_c_M}')
print(f'Medium Control (%)                : {df_c_M_P} %')

print(f'Range Control                     : {df_c_R}')
print(f'Range Control (%)                 : {df_c_R_P} %')

