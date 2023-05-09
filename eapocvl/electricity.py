# Parental status
import pandas as pd


df = pd.read_excel('~/Documents/EAPOCVL/_2023_05_07/CLIENTS_VARIABLE.xlsx')
# df = df.columns
# print(df)

# df = df['redcap_event_name'].value_counts()
# df = df['redcap_data_access_group'].value_counts()
# df = df['what_is_the_life_status_of'].value_counts()
# df = df['has_the_participant_ever'].value_counts()
# print(df)
df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]
# print(df)

df_T = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'sinza_hospital')]

df_L = df_T[(df_T['what_type_of_facilities_ex___1'] == 1) | (df_T['what_type_of_facilities_ex___2'] == 1) | (df_T['what_type_of_facilities_ex___1'] == 3) | (df_T['what_type_of_facilities_ex___1'] == 4) | (
    df_T['what_type_of_facilities_ex___1'] == 5) | (df_T['what_type_of_facilities_ex___1'] == 6) | (df_T['what_type_of_facilities_ex___1'] == 7) | (df_T['what_type_of_facilities_ex___1'] == 8) | (df_T['what_type_of_facilities_ex___1'] == 9)]

df_i_T = df_L[(df_L['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df_L['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df_c_T = df_L[(df_L['redcap_data_access_group'] == 'amana_hospital') | (
    df_L['redcap_data_access_group'] == 'sinza_hospital')]


df1 = df_L[(df_L['what_type_of_facilities_ex___9'] == 1)]

df1_i = df1[(df1['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df1['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]

df1_c = df1[(df1['redcap_data_access_group'] == 'amana_hospital')
            | (df1['redcap_data_access_group'] == 'sinza_hospital')]


df_L = df_L.shape[0]
df1 = df1.shape[0]
df_P = (df1 * 100) / (df_L)

df_i_T = df1_i.shape[0]
df_i_P = (df_i_T * 100) / (df_L)

df_c_T = df1_c.shape[0]
df_c_P = (df_c_T * 100) / (df_L)


# ## OUT PUT
print(f'')
print(f'"NIMR SITES - TANZANIA"')
print(f'"Parental status"')
print(f'')

print(f'Total Answers                           : {df1}')
print(f'Answers / Enrolled                      : {df_P} %')


print(f'')
print(f'Intervtn')
print(f'')

print(f'Total Intervtn                         : {df_i_T}')
print(f'Percentage Intervtn                    : {df_i_P} %')


print(f'')
print(f'Control')
print(f'')

print(f'Total Control                          : {df_c_T}')
print(f'Percentage Control                     : {df_c_P} %')
