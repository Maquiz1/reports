import pandas as pd
import numpy as np

df = pd.read_csv('/home/maquiz/Documents/EAPOVL/_2023_07_19/EAPOC.csv')
df2 = pd.read_csv('/home/maquiz/Documents/EAPOVL/_2023_07_19/EAPOC.csv')

# df = pd.read_excel('/home/maquiz/Documents/EAPOVL/_2023_07_02/CLIENTS.xlsx')

# df = df.columns
# df = df[(df['redcap_event_name'] == 'screening_arm_1')]
df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]
df = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'sinza_hospital') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]

df2 = df2[(df2['redcap_event_name'] == 'enrollment_v1_arm_1')]
df2 = df2[(df2['redcap_data_access_group'] == 'amana_hospital') | (df2['redcap_data_access_group'] == 'sinza_hospital') | (
    df2['redcap_data_access_group'] == 'mwananyamala_hospi') | (df2['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]


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


# HOW MANY CHILDREN
# df = df[df.do_you_have_your_own_child.isnull()]
# df = df[(df['do_you_have_your_own_child'] == 1)]
# df = df[df.how_many_children_do_you_h.isnull()]
# df = df[(df['how_many_children_do_you_h'] < 1)]

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

# # ADHERENCEN
# df = df[(df.provide_participants_most___1 == 0) & (df.provide_participants_most___2 == 0) & (
#     df.provide_participants_most___3 == 0) & (df.provide_participants_most___4 == 0)]

# df = df[['record_id', 'visit_date', 'provide_participants_most___1', 'provide_participants_most___2', 'provide_participants_most___3', 'provide_participants_most___4', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.14.xlsx')


# # ADHERENCEN A
# df = df[df.provide_participants_most___1 == 1]
# df = df[df.a_adherence_1.isnull()]

# df = df[['record_id', 'visit_date', 'provide_participants_most___1', 'a_adherence_1', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.14a.xlsx')

# df2 = df2[df2.provide_participants_most___1 == 1]
# df2 = df2[df2.adherence_1_date.isnull()]

# df2 = df2[['record_id', 'visit_date', 'provide_participants_most___1', 'adherence_1_date', 'redcap_data_access_group']
#           ].sort_values('redcap_data_access_group')
# df3 = df2.shape
# print(df2)
# print(df3)
# df2.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.14a2.xlsx')


# # ADHERENCEN B
# df = df[df.provide_participants_most___2 == 1]
# df = df[df.b_adherence_2.isnull()]

# df = df[['record_id', 'visit_date', 'provide_participants_most___2', 'b_adherence_2', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.14b.xlsx')

# df2 = df2[df2.provide_participants_most___2 == 1]
# df2 = df2[df2.adherence_2_date.isnull()]

# df2 = df2[['record_id', 'visit_date', 'provide_participants_most___2', 'adherence_2_date', 'redcap_data_access_group']
#           ].sort_values('redcap_data_access_group')
# df3 = df2.shape
# print(df2)
# print(df3)
# df2.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.14b2.xlsx')


# # ADHERENCEN C
# df = df[df.provide_participants_most___3 == 1]
# df = df[df.c_adherence_3.isnull()]

# df = df[['record_id', 'visit_date', 'provide_participants_most___3', 'c_adherence_3', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.14c.xlsx')

# df2 = df2[df2.provide_participants_most___3 == 1]
# df2 = df2[df2.adherence_3_date.isnull()]

# df2 = df2[['record_id', 'visit_date', 'provide_participants_most___3', 'adherence_3_date', 'redcap_data_access_group']
#           ].sort_values('redcap_data_access_group')
# df3 = df2.shape
# print(df2)
# print(df3)
# df2.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.14c2.xlsx')


# # Psychosocial STATUS
# df = df[df.does_the_participant_have.isnull()]
# df = df[['record_id', 'visit_date', 'does_the_participant_have', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.15.xlsx')

# # # Psychosocial type of support
# df = df[df.does_the_participant_have == 1]
# df = df[(df.if_yes_list_the_type_of_su___1 == 0) & (df.if_yes_list_the_type_of_su___2 == 0) &
#         (df.if_yes_list_the_type_of_su___3 == 0) & (df.if_yes_list_the_type_of_su___4 == 0) &
#         (df.if_yes_list_the_type_of_su___5 == 0) & (df.if_yes_list_the_type_of_su___6 == 0) &
#         (df.if_yes_list_the_type_of_su___7 == 0) & (df.if_yes_list_the_type_of_su___8 == 0) &
#         (df.if_yes_list_the_type_of_su___9 == 0)]

# df = df[['record_id', 'visit_date', 'if_yes_list_the_type_of_su___1', 'if_yes_list_the_type_of_su___2',
#        'if_yes_list_the_type_of_su___3', 'if_yes_list_the_type_of_su___4', 'if_yes_list_the_type_of_su___5',
#        'if_yes_list_the_type_of_su___6', 'if_yes_list_the_type_of_su___7', 'if_yes_list_the_type_of_su___8',
#        'if_yes_list_the_type_of_su___9', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.16.xlsx')


# # # Psychosocial type of support Other
# df = df[df.does_the_participant_have == 1]
# df = df[(df.if_yes_list_the_type_of_su___9 == 1)]
# df = df[df.if_other_specify_2.isnull()]


# df = df[['record_id', 'visit_date', 'does_the_participant_have','if_yes_list_the_type_of_su___9','if_other_specify_2', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.16_other.xlsx')


# # # intensive adherence counseling
# df = df[df.has_intensive_adherence_co.isnull()]


# df = df[['record_id', 'visit_date','has_intensive_adherence_co', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.17.xlsx')


# # intensive adherence counseling DATE
df = df[df.has_intensive_adherence_co == 1]
df = df[df.if_yes_when_was_intensive.isnull()]


df = df[['record_id', 'visit_date','has_intensive_adherence_co', 'if_yes_when_was_intensive','redcap_data_access_group']
        ].sort_values('redcap_data_access_group')
df1 = df.shape
print(df)
print(df1)
df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.18.xlsx')


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
