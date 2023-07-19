# Parental status
import pandas as pd


df = pd.read_excel('~/Documents/EAPOCVL/_2023_05_07/CLIENTS_VARIABLE.xlsx')
# df = df.columns
# print(df)

# df = df['redcap_event_name'].value_counts()
# df = df['redcap_data_access_group'].value_counts()
# df = df['what_is_the_life_status_of'].value_counts()
# df = df['redcap_event_name'].value_counts()
# print(df)


df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]


df_T = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'sinza_hospital')]

df_L = df_T[(df_T['e_1_a_age_in_years'] >= 0) & (df_T['e_1_a_age_in_years'] <= 24)]

df_i_T = df_L[(df_L['redcap_data_access_group'] == 'mwananyamala_hospi') | (df_L['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df_c_T = df_L[(df_L['redcap_data_access_group'] == 'amana_hospital') | (df_L['redcap_data_access_group'] == 'sinza_hospital')]


df_L = df_L['how_many_children_do_you_h']
df_M = df_L.median()
df_R = df_L.max() - df_L.min()
# df.groupby("ChildID").apply(lambda x: x['abdomcirc'].max() - x['abdomcirc'].min())


df_i_T = df_i_T['how_many_children_do_you_h']
df_i_M = df_i_T.median()
df_i_R = df_i_T.max() - df_i_T.min()

df_c_T = df_c_T['how_many_children_do_you_h']
df_c_M = df_c_T.median()
df_c_R = df_c_T.max() - df_c_T.min()


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
