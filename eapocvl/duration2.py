# Parental status
import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_excel('~/Documents/EAPOCVL/_2023_05_07/CLIENTS_VARIABLE.xlsx')


df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]


df_T = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'sinza_hospital')]

df_L = df_T[(df_T['when_did_the_participant_s'] != '')]

today = datetime.today().strftime('%Y-%m-%d')
df_L['today_date'] = today


df_L_today = df_L['today_date']
df_L_date = df_L['when_did_the_participant_s']

df_i_T = df_L[(df_L['redcap_data_access_group'] == 'mwananyamala_hospi') | (df_L['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df_c_T = df_L[(df_L['redcap_data_access_group'] == 'amana_hospital') | (df_L['redcap_data_access_group'] == 'sinza_hospital')]

df_L_i_today = df_i_T['today_date']
df_L_i_date = df_i_T['when_did_the_participant_s']

df_L_c_today = df_c_T['today_date']
df_L_c_date = df_c_T['when_did_the_participant_s']


df_L_today = pd.to_datetime(df_L_today)
df_L_date = pd.to_datetime(df_L_date)

df_L_i_today = pd.to_datetime(df_L_i_today)
df_L_i_date = pd.to_datetime(df_L_i_date)

df_L_c_today = pd.to_datetime(df_L_c_today)
df_L_c_date = pd.to_datetime(df_L_c_date)



years =  np.floor((df_L_today -  df_L_date).dt.days / 365.25)
yearsi =  np.floor((df_L_i_today -  df_L_i_date).dt.days / 365.25)
yearsc =  np.floor((df_L_c_today -  df_L_c_date).dt.days / 365.25)








df_M = years.median()
df_R = years.max() - years.min()

df_i_M = yearsi.median()
df_i_R = yearsi.max() - yearsi.min()

df_c_M = years.median()
df_c_R = yearsc.max() - yearsc.min()


# ## OUT PUT
print(f'')
print(f'"NIMR SITES - TANZANIA"')
print(f'"Parental status"')
print(f'')

print(f'Medium                            : {df_M}')
print(f'Range                             : {df_R}')

print(f'')
print(f'Intervtn')
print(f'')

print(f'Medium Intervtn                   : {df_i_M}')
print(f'Range Intervtn                    : {df_i_R} %')


print(f'')
print(f'Control')
print(f'')

print(f'Medium Control                    : {df_c_M}')
print(f'Range Control                     : {df_c_R} %')
