# Parental status
import pandas as pd


# df = pd.read_excel('~/Documents/EAPOCVL/_2023_05_07/CLIENTS_VARIABLE.xlsx')
df = pd.read_csv('/home/maquiz/Documents/EAPOVL/_2023_07_11/EAPOC.csv')



df_T = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'sinza_hospital')]


df_S = df_T[(df_T['c_visit_no'] == 1)]

df_E = df_T[(df_T['is_the_participant_eligibl_1'] == 1)]



df1 = df_S[(df_S['redcap_event_name'] == 'screening_arm_1')]

df1_1 = df1[(df1['redcap_data_access_group'] == 'sinza_hospital')]
df1_2 = df1[(df1['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df1_3 = df1[(df1['redcap_data_access_group'] == 'amana_hospital')]
df1_4 = df1[(df1['redcap_data_access_group'] == 'mwananyamala_hospi')]

df2 = df_E[(df_E['redcap_event_name'] == 'enrollment_v1_arm_1')]

df2_1 = df2[(df2['redcap_data_access_group'] == 'sinza_hospital')]
df2_2 = df2[(df2['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df2_3 = df2[(df2['redcap_data_access_group'] == 'amana_hospital')]
df2_4 = df2[(df2['redcap_data_access_group'] == 'mwananyamala_hospi')]



df1_i = df1[(df1['redcap_data_access_group'] == 'mwananyamala_hospi') | (df1['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df2_i = df2[(df2['redcap_data_access_group'] == 'mwananyamala_hospi') | (df2['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]


df1_c = df1[(df1['redcap_data_access_group'] == 'amana_hospital') | (df1['redcap_data_access_group'] == 'sinza_hospital')]
df2_c = df2[(df2['redcap_data_access_group'] == 'amana_hospital') | (df2['redcap_data_access_group'] == 'sinza_hospital')]


df_S = df_S.shape[0]

df_E = df_E.shape[0]

df1_i = df1_i.shape[0]

df2_i = df2_i.shape[0]

df1_c = df1_c.shape[0]

df1_1 = df1_1.shape[0]
df2_1 = df2_1.shape[0]


df1_2 = df1_2.shape[0]
df2_2 = df2_2.shape[0]

df1_3 = df1_3.shape[0]
df2_3 = df2_3.shape[0]

df1_4 = df1_4.shape[0]
df2_4 = df2_4.shape[0]


# ## OUT PUT
print(f'')
print(f'"NIMR SITES - TANZANIA"')
print(f'"status"')
print(f'')

print(f'')
print(f'Total')
print(f'')

print(f'Total screend                          : {df_S}')
print(f'Total Enrolled                         : {df_E}')


print(f'')
print(f'Intervention')
print(f'')

print(f'Total screend                          : {df1_i}')
print(f'Total Enrolled                         : {df2_i}')

print(f'')
print(f'Control')
print(f'')

print(f'Total screend                          : {df1_c}')
print(f'Total Enrolled                         : {df2_c}')


print(f'')
print(f'Screening & Enrollment')
print(f'')

print(f'Sinza Screened                        : {df1_1} ')
print(f'Sinza Enrolled                        : {df2_1} %')

print(f'Mnazi Screened                        : {df1_2} ')
print(f'Mnazi Enrolled                        : {df2_2} %')


print(f'Amana Screened                        : {df1_3} ')
print(f'Amana Enrolled                        : {df2_3} %')


print(f'Mwananyamala Screened                 : {df1_4} ')
print(f'Mwananyamala Enrolled                 : {df2_4} %')



