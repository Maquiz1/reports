import pandas as pd
import numpy as np

df = pd.read_csv('/home/maquiz/Documents/EAPOVL/_2023_07_19/EAPOC.csv')
# df = pd.read_excel('/home/maquiz/Documents/EAPOVL/_2023_07_02/CLIENTS.xlsx')

# df = df.columns
# df = df[(df['redcap_event_name'] == 'screening_arm_1')]
df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]
df = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'sinza_hospital') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]


# ENROLLMENT
# df = df[df.has_the_participant_ever.isnull()]
# df = df[df.is_the_participant_still_i.isnull()]

# SCHOOL CURRENT MISSING
# df = df[(df['has_the_participant_ever'] == 1)]
# df = df[df.is_the_participant_still_i.isnull()]

# # EMPLYOMENT
# # df = df[df.is_the_participnt_in_any.isnull()]

# df = df[(df['is_the_participnt_in_any'] == 1) & (df.what_is_the_main_occupatio.isnull())]
# df = df[['record_id', 'visit_date', 'is_the_participnt_in_any', 'what_is_the_main_occupatio', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/1.13.xlsx')

# MARITAL STATUS
# df = df[df.marital_status.isnull()]
# df = df[['record_id', 'visit_date', 'marital_status', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/1.14.xlsx')


# # HAVING CHILDREN
# df = df[(df['marital_status'] != 5)]
# df = df[df.do_you_have_your_own_child.isnull()]
# df = df[['record_id', 'visit_date', 'do_you_have_your_own_child', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/1.15.xlsx')


HOW MANY CHILDREN
df = df[df.do_you_have_your_own_child.isnull()]
df = df[(df['do_you_have_your_own_child'] == 1)]
df = df[df.how_many_children_do_you_h.isnull()]
df = df[(df['how_many_children_do_you_h'] < 1)]

# df = df[['record_id', 'visit_date', 'do_you_have_your_own_child', 'how_many_children_do_you_h','redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/1.16.xlsx')


# # LIVING WITH CHILDREN
# df = df[df.do_you_have_your_own_child.isnull()]
# df = df[(df['do_you_have_your_own_child'] == 1)]
# df = df[df.how_many_of_your_children.isnull()]

# df = df[['record_id', 'visit_date', 'do_you_have_your_own_child', 'how_many_children_do_you_h','how_many_of_your_children','redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/1.17.xlsx')

# ADHERENCEN
df = df[df.provide_participants_most.isnull()]
# df = df[(df['do_you_have_your_own_child'] == 1)]
# df = df[df.how_many_children_do_you_h.isnull()]
# df = df[(df['how_many_children_do_you_h'] < 1)]

df = df[['record_id', 'visit_date', 'provide_participants_most','redcap_data_access_group']
        ].sort_values('redcap_data_access_group')
df1 = df.shape
print(df)
print(df1)
df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.14.xlsx')


# EAPOCVL SYSTEMS

# df = df[['study_id', 'age', 'gender', 'marital_status',
#          'education_level', 'occupation', 'site_id', 'recent_vl', 'recent_vl_date', 'vl', 'vl_date']]


# all_columns = list(df) # Creates list of all column headers
# df[all_columns] = df[all_columns].astype(str)

# df = df[df.what_is_the_estimatd_dura.notnull()]
# df[['what_is_the_estimatd_dura']] = df[['what_is_the_estimatd_dura']].astype('int')

# df = df[df['what_is_the_estimatd_dura'] < 6]


# START ART
# df = df[df.when_did_the_participant_s.notnull()]
# df['DateTime1'] = pd.to_datetime(df['visit_date'])
# df['DateTime2'] = pd.to_datetime(df['when_did_the_participant_s'])
# df['nb_months'] = ((df.DateTime1 - df.DateTime2)/np.timedelta64(1, 'M'))
# df['nb_months'] = df['nb_months'].astype('int')
# df[df['nb_months'] < 6]


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

