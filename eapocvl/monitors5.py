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

# # first time diagnosed with HIV

# df = df[(df.when_was_the_participant_f.isnull()) | (
#     df.when_was_the_participant_f.isna()) | (df.when_was_the_participant_f == ' ')]

# df = df[['record_id', 'visit_date', 'when_was_the_participant_f',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/1.18.xlsx')


# # estimated duration (months) since HIV diagnosis when date missing
# df = df[(df.when_did_the_participant_s.isnull()) | (
#     df.when_did_the_participant_s.isna()) | (df.when_did_the_participant_s == ' ')]

# df = df[(df.what_is_the_estimated_dura.isnull()) | (
#     df.what_is_the_estimated_dura.isna()) | (df.what_is_the_estimated_dura == ' ')]

# df = df[['record_id', 'visit_date', 'when_did_the_participant_s', 'what_is_the_estimated_dura',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])

# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/1.19 IF DATE NOT KNOWN.xlsx')


# # Start taking ART
# df = df[(df.when_did_the_participant_s.isnull()) | (
#     df.when_did_the_participant_s.isna()) | (df.when_did_the_participant_s == ' ')]

# df = df[['record_id', 'visit_date', 'when_did_the_participant_s',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])

# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/1.20.xlsx')


# # DURATION SINCE ART IF DATE NOT KNOWNS
# df = df[(df.when_did_the_participant_s.isnull()) | (
#     df.when_did_the_participant_s.isna()) | (df.when_did_the_participant_s == ' ')]

# df = df[(df.what_is_the_estimatd_dura.isnull()) | (
#     df.what_is_the_estimatd_dura.isna()) | (df.what_is_the_estimatd_dura == ' ')]

# df = df[['record_id', 'visit_date', 'what_is_the_estimatd_dura',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])

# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/1.21 IF DATE NOT KNOWNS.xlsx')


# # DURATION ON Current ART regimen MISSING?
# df = df[(df.how_long_has_the_participa.isnull()) | (
#     df.how_long_has_the_participa.isna()) | (df.how_long_has_the_participa == ' ')]

# df = df[['record_id', 'visit_date', 'how_long_has_the_participa',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])

# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.7.xlsx')


# # REGIME taking since starting ART MISSING ?
# df = df[(df.is_this_the_regimen_the_pa.isnull()) | (
#     df.is_this_the_regimen_the_pa.isna()) | (df.is_this_the_regimen_the_pa == ' ')]

# # df = df[(df.is_this_the_regimen_the_pa == 1)]

# df = df[['record_id', 'visit_date','is_this_the_regimen_the_pa',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])

# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.9 .xlsx')


# DURATION ON Current ART regimen IF CURRENT IS FIRST?
# df = df[(df.is_this_the_regimen_the_pa == 1)]

# df['how_long_has_the_participa'] = df['how_long_has_the_participa'].astype('int')
# df = df[df.how_long_has_the_participa.lt(6)]

# df = df[['record_id', 'visit_date','is_this_the_regimen_the_pa', 'how_long_has_the_participa',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])

# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.7 if Current is First.xlsx')



# DURATION SINCE STARTING ART regimen PART 2?

# df['DateTime1'] = pd.to_datetime(df['visit_date'])
# df['DateTime2'] = pd.to_datetime(df['when_did_the_participant_s'])
# df['nb_months'] = ((df.DateTime1 - df.DateTime2)/np.timedelta64(1, 'M'))
# df['nb_months'] = df['nb_months'].astype('int')
# df = df[df.nb_months.lt(6)]

# df = df[['record_id', 'visit_date','when_did_the_participant_s', 'nb_months',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])

# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_20/2.7 DURATION SINCE ART.xlsx')




# START VIRAL LOAD
# df = df[df.what_is_the_most_recent_vi.isnull()]
# df['what_is_the_most_recent_vi'] = df['what_is_the_most_recent_vi'].astype('str')
# df[df['what_is_the_most_recent_vi'] < '50']

# df = df[df.visit_date.isnull()]
# df = df[df.when_was_the_sample_for_th.isnull()]
# df = df[df.what_is_the_most_recent_vi.isnull()]
# df = df[df.when_was_the_vl_result_giv.isnull()]


# VIRAL LOAD DURATION
# df['DateTime1'] = pd.to_datetime(df['visit_date'])
# df['DateTime2'] = pd.to_datetime(df['when_was_the_sample_for_th'])
# df['nb_months'] = ((df.DateTime1 - df.DateTime2)/np.timedelta64(1, 'M'))
# df['nb_months'] = df['nb_months'].astype('int')
# df[df['nb_months'] < 6]

# REDCAP
# df = df[['record_id', 'visit_date', 'when_did_the_participant_s','nb_months', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')

# df = df[['record_id', 'visit_date', 'when_was_the_sample_for_th','what_is_the_most_recent_vi','nb_months', 'redcap_data_access_group']
#         ].sort_values(by=['redcap_data_access_group', 'nb_months'])
