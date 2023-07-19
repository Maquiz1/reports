# Parental status
import pandas as pd


# df = pd.read_excel('~/Documents/EAPOCVL/_2023_05_15/CLIENTS.xlsx')
# df = pd.read_csv('/Documents/EAPOVL/_2023_06_26/EAPOVL.csv')
df = pd.read_csv('/home/maquiz/Documents/EAPOVL/_2023_07_02/EAPOC.csv')


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

df_L = df_T[(df_T['e_1_a_age_in_years'] >= 0) &
            (df_T['e_1_a_age_in_years'] <= 24)]

df_sum_T = df_L[(df_L['e_1_a_age_in_years'] >= 0) &
                (df_L['e_1_a_age_in_years'] <= 24)]


df_i_T = df_L[(df_L['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df_L['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df_c_T = df_L[(df_L['redcap_data_access_group'] == 'amana_hospital') | (
    df_L['redcap_data_access_group'] == 'sinza_hospital')]

df_sum_I = df_i_T[(df_i_T['e_1_a_age_in_years'] >= 0) &
                  (df_i_T['e_1_a_age_in_years'] <= 24)]
df_sum_C = df_c_T[(df_c_T['e_1_a_age_in_years'] >= 0) &
                  (df_c_T['e_1_a_age_in_years'] <= 24)]


df_sum_T = df_sum_T['e_1_a_age_in_years'].sum()

df_sum_I = df_sum_I['e_1_a_age_in_years'].sum()
df_sum_I_P = (df_sum_I * 100) / (df_sum_T)

df_sum_C = df_sum_C['e_1_a_age_in_years'].sum()
df_sum_C_P = (df_sum_C * 100) / (df_sum_T)


df1 = df_L[(df_L['e_1_a_age_in_years'] >= 0) &
           (df_L['e_1_a_age_in_years'] <= 12)]
df2 = df_L[(df_L['e_1_a_age_in_years'] >= 13) &
           (df_L['e_1_a_age_in_years'] <= 19)]
df3 = df_L[(df_L['e_1_a_age_in_years'] >= 20) &
           (df_L['e_1_a_age_in_years'] <= 24)]


df1_i = df1[(df1['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df1['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df2_i = df2[(df2['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df2['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df3_i = df3[(df3['redcap_data_access_group'] == 'mwananyamala_hospi') | (
    df3['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]

df1_c = df1[(df1['redcap_data_access_group'] == 'amana_hospital')
            | (df1['redcap_data_access_group'] == 'sinza_hospital')]
df2_c = df2[(df2['redcap_data_access_group'] == 'amana_hospital')
            | (df2['redcap_data_access_group'] == 'sinza_hospital')]
df3_c = df3[(df3['redcap_data_access_group'] == 'amana_hospital')
            | (df3['redcap_data_access_group'] == 'sinza_hospital')]


df_L = df_L.shape[0]
df_P = (df_L * 100) / (df_L)

df_i_T = df_i_T.shape[0]
df_i_P = (df_i_T * 100) / (df_L)

df_c_T = df_c_T.shape[0]
df_c_P = (df_c_T * 100) / (df_L)


df1_T = df1.shape[0]
df1_P = (df1_T * 100) / (df_L)

df2_T = df2.shape[0]
df2_P = (df2_T * 100) / (df_L)

df3_T = df3.shape[0]
df3_P = (df3_T * 100) / (df_L)


df1_i_T = df1_i.shape[0]
df1_i_P = (df1_i_T * 100) / (df1_T)

df2_i_T = df2_i.shape[0]
df2_i_P = (df2_i_T * 100) / (df2_T)

df3_i_T = df3_i.shape[0]
df3_i_P = (df3_i_T * 100) / (df3_T)


df1_c_T = df1_c.shape[0]
df1_c_P = (df1_c_T * 100) / (df1_T)

df2_c_T = df2_c.shape[0]
df2_c_P = (df2_c_T * 100) / (df2_T)

df3_c_T = df3_c.shape[0]
df3_c_P = (df3_c_T * 100) / (df3_T)

# ## OUT PUT
print(f'')
print(f'"NIMR SITES - TANZANIA"')
print(f'"Parental status"')
print(f'')
print(f'Total age                               : {df_sum_T}')
print(f'Total age (Intervention)                : {df_sum_I}')
print(f'Total age (Percentage)                  : {df_sum_I_P}')
print(f'Total age (Control)                     : {df_sum_C}')
print(f'Total age (Percentage)                  : {df_sum_C_P}')


print(f'Total Answers                           : {df_L}')
print(f'Total Enrolled                          : {df_L}')
print(f'Answers / Enrolled                      : {df_P} %')

print(f'')
print(f'Total')
print(f'')


print(f'0-12 yrs                                : {df1_T} ')
print(f'0-12 yrs                                : {df1_P} %')

print(f'13-19 yrs                               : {df2_T}')
print(f'13-19 yrs                               : {df2_P} %')

print(f'20-24 yrs                               : {df3_T}')
print(f'20-24 yrs                               : {df3_P} %')


print(f'')
print(f'Intervtn')
print(f'')

print(f'Total Intervtn                         : {df_i_T}')
print(f'Percentage Intervtn                    : {df_i_P} %')

print(f'')

print(f'0-12 yrs (Intervtn)                    : {df1_i_T}')
print(f'0-12 yrs (Intervtn)                    : {df1_i_P} %')

print(f'13-19 yrs (Intervtn)                   : {df2_i_T}')
print(f'13-19 yrs (Intervtn)                   : {df2_i_P} %')

print(f'20-24 yrs (Intervtn)                   : {df3_i_T}')
print(f'20-24 yrs (Intervtn)                   : {df3_i_P} %')


print(f'')
print(f'Control')
print(f'')

print(f'Total Control                          : {df_c_T}')
print(f'Percentage Control                     : {df_c_P} %')

print(f'')

print(f'0-12 yrs (Control)                     : {df1_c_T}')
print(f'0-12 yrs (Control)                     : {df1_c_P} %')

print(f'13-19 yrs (Control)                    : {df2_c_T}')
print(f'13-19 yrs (Control)                    : {df2_c_P} %')

print(f'20-24 yrs (Control)                    : {df3_c_T}')
print(f'20-24 yrs (Control)                    : {df3_c_P} %')
