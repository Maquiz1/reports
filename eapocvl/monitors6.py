import pandas as pd
import numpy as np

df = pd.read_csv('/home/maquiz/Documents/EAPOVL/_2023_07_19/EAPOC.csv')
# df = pd.read_excel('/home/maquiz/Documents/EAPOVL/_2023_07_02/CLIENTS.xlsx')

# df = df.columns
# df = df[(df['redcap_event_name'] == 'screening_arm_1')]
df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]
df = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'sinza_hospital') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]


# EAPOCVL SYSTEMS

# df = df[['study_id', 'age', 'gender', 'marital_status',
#          'education_level', 'occupation', 'site_id', 'recent_vl', 'recent_vl_date', 'vl', 'vl_date']]


# REDCAP

# # recent viral load result missing

# df = df[(df.what_is_the_most_recent_vi.isnull()) | (
#     df.what_is_the_most_recent_vi.isna()) | (df.what_is_the_most_recent_vi == ' ')]

# df = df[['record_id', 'visit_date', 'what_is_the_most_recent_vi',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.9 missing.xlsx')


# # recent viral load result less than 50

# df['what_is_the_most_recent_vi'] = df['what_is_the_most_recent_vi'].astype('str')
# df = df[df.what_is_the_most_recent_vi != '3480CP/ML']
# df['what_is_the_most_recent_vi'] = df['what_is_the_most_recent_vi'].astype('int')

# df = df[df.what_is_the_most_recent_vi.lt(50)]

# df = df[['record_id', 'visit_date', 'what_is_the_most_recent_vi',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.9 less than 50.xlsx')



# # recent viral load date missing

# df = df[(df.when_was_the_sample_for_th.isnull()) | (
#     df.when_was_the_sample_for_th.isna()) | (df.when_was_the_sample_for_th == ' ')]

# df = df[['record_id', 'visit_date', 'when_was_the_sample_for_th',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.10 missing.xlsx')


# VL result received by the study site missing

# df = df[(df.when_was_the_vl_result_rec.isnull()) | (
#     df.when_was_the_vl_result_rec.isna()) | (df.when_was_the_vl_result_rec == ' ')]

# df = df[['record_id', 'visit_date', 'when_was_the_vl_result_rec',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.11 missing.xlsx')


# # VL result given by the study site to client missing

# df = df[(df.when_was_the_vl_result_giv.isnull()) | (
#     df.when_was_the_vl_result_giv.isna()) | (df.when_was_the_vl_result_giv == ' ')]

# df = df[['record_id', 'visit_date', 'when_was_the_vl_result_giv',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.12 missing.xlsx')

# # VL result given by the study site to client missing

# df = df[(df.when_was_the_vl_result_giv.isnull()) | (
#     df.when_was_the_vl_result_giv.isna()) | (df.when_was_the_vl_result_giv == ' ')]

# df = df[['record_id', 'visit_date', 'when_was_the_vl_result_giv',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.12 missing.xlsx')



# # most recent CD4 count missing

# df = df[(df.what_is_the_participant_s.isnull()) | (
#     df.what_is_the_participant_s.isna()) | (df.what_is_the_participant_s == ' ')]

# df = df[['record_id', 'visit_date', 'what_is_the_participant_s',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.13 missing.xlsx')


# # Check the most recent result and date sample taken missing

# df = df[(df.a_check_most_recent_result.isnull()) | (
#     df.a_check_most_recent_result.isna()) | (df.a_check_most_recent_result == ' ')]

# df = df[['record_id', 'visit_date', 'a_check_most_recent_result',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.13a missing.xlsx')


# VIRAL LOAD DURATION difference
df = df[~df.when_was_the_sample_for_th.str.contains('323-01-01')]

df['DateTime1'] = pd.to_datetime(df['visit_date'])
df['DateTime2'] = pd.to_datetime(df['when_was_the_sample_for_th'])
df['nb_months'] = ((df.DateTime1 - df.DateTime2)/np.timedelta64(1, 'M'))
df['nb_months'] = df['nb_months'].astype(int)
df = df[df.nb_months.gt(6)]

df = df[['record_id', 'visit_date','when_was_the_sample_for_th','nb_months',
         'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])

df1 = df.shape
print(df)
print(df1)
df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/MORE THA 6  SINCE VIRAL SAMPLE TAKEN.xlsx')


