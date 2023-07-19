# Parental status
import pandas as pd


df = pd.read_excel('~/Documents/EAPOCVL/_2023_05_07/CLIENTS_VARIABLE.xlsx')
# df = df.columns
# print(df)

# df = df['redcap_event_name'].value_counts()
# df = df['redcap_data_access_group'].value_counts()
# df = df['what_is_the_life_status_of'].value_counts()
# df = df['which_art_regimen_is_the_p'].value_counts()
# print(df)
df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]
# print(df)

df_T = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'sinza_hospital')]

df_L = df_T[(df_T['whom_does_the_participant'] == 1) | (df_T['whom_does_the_participant'] == 2) | (
    df_T['whom_does_the_participant'] == 3) | (df_T['whom_does_the_participant'] == 4) | (df_T['whom_does_the_participant'] == 5) | (df_T['whom_does_the_participant'] == 6) | (df_T['whom_does_the_participant'] == 7) | (df_T['whom_does_the_participant'] == 8)]

df_i_T = df_L[(df_L['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df_L['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df_c_T = df_L[(df_L['redcap_data_access_group'] == 'amana_hospital') | (
    df_L['redcap_data_access_group'] == 'sinza_hospital')]


df1 = df_L[(df_L['whom_does_the_participant'] == 1)]
df2 = df_L[(df_L['whom_does_the_participant'] == 2)]
df3 = df_L[(df_L['whom_does_the_participant'] == 3)]
df4 = df_L[(df_L['whom_does_the_participant'] == 4)]
df5 = df_L[(df_L['whom_does_the_participant'] == 5)]
df6 = df_L[(df_L['whom_does_the_participant'] == 6)]
df7 = df_L[(df_L['whom_does_the_participant'] == 7)]
df8 = df_L[(df_L['whom_does_the_participant'] == 8)]



df1_i = df1[(df1['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df1['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df2_i = df2[(df2['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df2['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df3_i = df3[(df3['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df3['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df4_i = df4[(df4['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df4['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df5_i = df5[(df5['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df5['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df6_i = df6[(df6['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df6['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df7_i = df7[(df7['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df7['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df8_i = df8[(df8['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df8['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]


df1_c = df1[(df1['redcap_data_access_group'] == 'amana_hospital')
            | (df1['redcap_data_access_group'] == 'sinza_hospital')]
df2_c = df2[(df2['redcap_data_access_group'] == 'amana_hospital')
            | (df2['redcap_data_access_group'] == 'sinza_hospital')]
df3_c = df3[(df3['redcap_data_access_group'] == 'amana_hospital')
            | (df3['redcap_data_access_group'] == 'sinza_hospital')]
df4_c = df4[(df4['redcap_data_access_group'] == 'amana_hospital')
            | (df4['redcap_data_access_group'] == 'sinza_hospital')]
df5_c = df5[(df5['redcap_data_access_group'] == 'amana_hospital')
            | (df5['redcap_data_access_group'] == 'sinza_hospital')]
df6_c = df6[(df6['redcap_data_access_group'] == 'amana_hospital')
            | (df6['redcap_data_access_group'] == 'sinza_hospital')]
df7_c = df7[(df7['redcap_data_access_group'] == 'amana_hospital')
            | (df7['redcap_data_access_group'] == 'sinza_hospital')]
df8_c = df8[(df8['redcap_data_access_group'] == 'amana_hospital')
            | (df8['redcap_data_access_group'] == 'sinza_hospital')]


df_T = df_T.shape[0]
df_L = df_L.shape[0]
df_P = (df_L * 100) / (df_T)

df_i_T = df_i_T.shape[0]
df_i_P = (df_i_T * 100) / (df_T)

df_c_T = df_c_T.shape[0]
df_c_P = (df_c_T * 100) / (df_T)


df1_T = df1.shape[0]
df1_P = (df1_T * 100) / (df_L)

df2_T = df2.shape[0]
df2_P = (df2_T * 100) / (df_L)

df3_T = df3.shape[0]
df3_P = (df3_T * 100) / (df_L)

df4_T = df4.shape[0]
df4_P = (df4_T * 100) / (df_L)

df5_T = df5.shape[0]
df5_P = (df5_T * 100) / (df_L)

df6_T = df6.shape[0]
df6_P = (df6_T * 100) / (df_L)

df7_T = df7.shape[0]
df7_P = (df7_T * 100) / (df_L)

df8_T = df8.shape[0]
df8_P = (df8_T * 100) / (df_L)


df1_i_T = df1_i.shape[0]
df1_i_P = (df1_i_T * 100) / (df1_T)

df2_i_T = df2_i.shape[0]
df2_i_P = (df2_i_T * 100) / (df2_T)

df3_i_T = df3_i.shape[0]
df3_i_P = (df3_i_T * 100) / (df3_T)

df4_i_T = df4_i.shape[0]
df4_i_P = (df4_i_T * 100) / (df4_T)

df5_i_T = df5_i.shape[0]
df5_i_P = (df5_i_T * 100) / (df5_T)

df6_i_T = df6_i.shape[0]
df6_i_P = (df6_i_T * 100) / (df6_T)

df7_i_T = df7_i.shape[0]
df7_i_P = (df7_i_T * 100) / (df7_T)

df8_i_T = df8_i.shape[0]
df8_i_P = (df8_i_T * 100) / (df8_T)


df1_c_T = df1_c.shape[0]
df1_c_P = (df1_c_T * 100) / (df1_T)

df2_c_T = df2_c.shape[0]
df2_c_P = (df2_c_T * 100) / (df2_T)

df3_c_T = df3_c.shape[0]
df3_c_P = (df3_c_T * 100) / (df3_T)

df4_c_T = df4_c.shape[0]
df4_c_P = (df4_c_T * 100) / (df4_T)

df5_c_T = df5_c.shape[0]
df5_c_P = (df5_c_T * 100) / (df5_T)

df6_c_T = df6_c.shape[0]
df6_c_P = (df6_c_T * 100) / (df6_T)

df7_c_T = df7_c.shape[0]
df7_c_P = (df7_c_T * 100) / (df7_T)

df8_c_T = df8_c.shape[0]
df8_c_P = (df8_c_T * 100) / (df8_T)

# ## OUT PUT
print(f'')
print(f'"NIMR SITES - TANZANIA"')
print(f'"Parental status"')
print(f'')

print(f'Total Answers                           : {df_L}')
print(f'Total Enrolled                          : {df_T}')
print(f'Answers / Enrolled                      : {df_P} %')

print(f'')
print(f'Total')
print(f'')


print(f'Both parents                         : {df1_T} ')
print(f'Both parents                         : {df1_P} %')

print(f'Grandparent                          : {df2_T}')
print(f'Grandparent                          : {df2_P} %')

print(f'Sibling                              : {df3_T}')
print(f'Sibling                              : {df3_P} %')

print(f'Other relative                       : {df4_T}')
print(f'Other relative                       : {df4_P} %')

print(f'Guardian/no kin relationship         : {df5_T}')
print(f'Guardian/no kin relationship         : {df5_P} %')

print(f'Lives alone                          : {df6_T}')
print(f'Lives alone                          : {df6_P} %')

print(f'Spouse/ partner                      : {df7_T}')
print(f'Spouse/ partner                      : {df7_P} %')

print(f'Other                                : {df8_T}')
print(f'Other                                : {df8_P} %')

print(f'')
print(f'Intervtn')
print(f'')

print(f'Total Intervtn                         : {df_i_T}')
print(f'Percentage Intervtn                    : {df_i_P} %')

print(f'')

print(f'Both parents (Intervtn)                   : {df1_i_T}')
print(f'Both parents (Intervtn)                   : {df1_i_P} %')

print(f'Grandparent (Intervtn)                    : {df2_i_T}')
print(f'Grandparent (Intervtn)                    : {df2_i_P} %')

print(f'Sibling    (Intervtn)                     : {df3_i_T}')
print(f'Sibling    (Intervtn)                     : {df3_i_P} %')

print(f'Other relative (Intervtn)                 : {df4_i_T}')
print(f'Other relative (Intervtn)                 : {df4_i_P} %')

print(f'Guardian/no kin relationship (Intervtn)   : {df5_i_T} %')
print(f'Guardian/no kin relationship (Intervtn)   : {df5_i_P} %')

print(f'Lives alone                               : {df6_i_T}')
print(f'Lives alone                               : {df6_i_P} %')

print(f'Spouse/ partner                           : {df7_i_T}')
print(f'Spouse/ partner                           : {df7_i_P} %')

print(f'Other                                     : {df8_i_T}')
print(f'Other                                     : {df8_i_P} %')


print(f'')
print(f'Control')
print(f'')

print(f'Total Control                          : {df_c_T}')
print(f'Percentage Control                     : {df_c_P} %')

print(f'')

print(f'Both parents (Control)                   : {df1_c_T}')
print(f'Both parents (Control)                   : {df1_c_P} %')

print(f'Grandparent (Control)                    : {df2_c_T}')
print(f'Grandparent (Control)                    : {df2_c_P} %')

print(f'Sibling    (Control)                     : {df3_c_T}')
print(f'Sibling    (Control)                     : {df3_c_P} %')

print(f'Other relative (Control)                 : {df4_c_T}')
print(f'Other relative (Intervtn)                : {df4_c_P} %')

print(f'Guardian/no kin relationship (Control)   : {df5_c_T} %')
print(f'Guardian/no kin relationship (Control)   : {df5_c_P} %')

print(f'Lives alone                               : {df6_c_T}')
print(f'Lives alone                               : {df6_c_P} %')

print(f'Spouse/ partner                           : {df7_c_T}')
print(f'Spouse/ partner                           : {df7_c_P} %')

print(f'Other                                     : {df7_c_T}')
print(f'Other                                     : {df8_c_P} %')
