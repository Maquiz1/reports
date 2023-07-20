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


# SCHOOL 

# df = df[(df.has_the_participant_ever.isnull()) | (df['has_the_participant_ever'] == ' ')]

# df = df[['record_id', 'visit_date', 'has_the_participant_ever', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/1.9.xlsx')

# # SCHOOL CURRENT MISSING
# df = df[(df['has_the_participant_ever'] == 1)]
# df = df[df.is_the_participant_still_i.isnull()]

# df = df[['record_id', 'visit_date', 'has_the_participant_ever', 'is_the_participant_still_i', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/1.10.xlsx')

# # EDUCATIONS  
# df = df[df.has_the_participant_ever == 1]
# df = df[(df.what_is_the_highest_level.isnull()) | (df['what_is_the_highest_level'] == ' ')]

# df = df[['record_id', 'visit_date','has_the_participant_ever', 'what_is_the_highest_level', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/1.11.xlsx')

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

# # Psychosocial type of support
# df = df[df.does_the_participant_have == 1]
# df = df[(df.if_yes_list_the_type_of_su___1 == 0) & (df.if_yes_list_the_type_of_su___2 == 0) &
#         (df.if_yes_list_the_type_of_su___3 == 0) & (df.if_yes_list_the_type_of_su___4 == 0) &
#         (df.if_yes_list_the_type_of_su___5 == 0) & (df.if_yes_list_the_type_of_su___6 == 0) &
#         (df.if_yes_list_the_type_of_su___7 == 0) & (df.if_yes_list_the_type_of_su___8 == 0) &
#         (df.if_yes_list_the_type_of_su___9 == 0)]

# df = df[['record_id', 'visit_date','does_the_participant_have', 'if_yes_list_the_type_of_su___1', 'if_yes_list_the_type_of_su___2',
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


# # # intensive adherence counseling DATE
# df = df[df.has_intensive_adherence_co == 1]
# df = df[df.if_yes_when_was_intensive.isnull()]


# df = df[['record_id', 'visit_date','has_intensive_adherence_co', 'if_yes_when_was_intensive','redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.18.xlsx')


# # # Psychosocial type of support
# df = df[(df.list_the_source_of_individ___1 == 0) & (df.list_the_source_of_individ___2 == 0) &
#         (df.list_the_source_of_individ___3 == 0) & (df.list_the_source_of_individ___4 == 0) &
#         (df.list_the_source_of_individ___5 == 0) & (df.list_the_source_of_individ___6 == 0)]

# df = df[['record_id', 'visit_date', 'list_the_source_of_individ___1', 'list_the_source_of_individ___2',
#        'list_the_source_of_individ___3', 'list_the_source_of_individ___4', 'list_the_source_of_individ___5',
#        'list_the_source_of_individ___6','redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.19.xlsx')


# # # Psychosocial type of support Other
# df = df[(df.list_the_source_of_individ___6 == 1)]
# df = df[df.if_other_specify_1.isnull()]


# df = df[['record_id', 'visit_date', 'list_the_source_of_individ___6','if_other_specify_1',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.19 other.xlsx')

# # DISTANCE
# df = df[df.how_far_does_the_participa.isnull()]


# df = df[['record_id', 'visit_date', 'how_far_does_the_participa',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.20.xlsx')


# # PARENTS STATUS
# df = df[(df.what_is_the_life_status_of.isnull()) | (df.what_is_the_life_status_of == ' ')]

# df = df[['record_id', 'visit_date', 'what_is_the_life_status_of',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.21.xlsx')


# # # PARENTS LIVING
# df = df[(df.whom_does_the_participant.isnull()) | (df.whom_does_the_participant == ' ')]

# df = df[['record_id', 'visit_date', 'whom_does_the_participant',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.22 .xlsx')


# # # PARENTS LIVING Other
# df = df[(df.whom_does_the_participant == 8)]
# df = df[df.specify_3.isnull()]


# df = df[['record_id', 'visit_date', 'whom_does_the_participant','specify_3',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.22 other.xlsx')


# # # Psychosocial type of support Other
# df = df[df.do_you_your_family_or_guar.isnull()]


# df = df[['record_id', 'visit_date', 'do_you_your_family_or_guar',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.23.xlsx')


# # # FACILITY EXISTS
# df = df[(df.what_type_of_facilities_ex___1 == 0) & (df.what_type_of_facilities_ex___2 == 0) &
#         (df.what_type_of_facilities_ex___3 == 0) & (df.what_type_of_facilities_ex___4 == 0) &
#         (df.what_type_of_facilities_ex___5 == 0) & (df.what_type_of_facilities_ex___6 == 0) &
#         (df.what_type_of_facilities_ex___7 == 0) & (df.what_type_of_facilities_ex___8 == 0)]

# df = df[['record_id', 'visit_date', 'what_type_of_facilities_ex___1', 'what_type_of_facilities_ex___2',
#        'what_type_of_facilities_ex___3', 'what_type_of_facilities_ex___4', 'what_type_of_facilities_ex___5',
#        'what_type_of_facilities_ex___6', 'what_type_of_facilities_ex___7', 'what_type_of_facilities_ex___8',
#        'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.24.xlsx')


# # # COMMENTS
# df = df[df.relevant_comments_on_parti.isnull()]


# df = df[['record_id', 'visit_date', 'relevant_comments_on_parti',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.25.xlsx')


# # # COMMENTS YES
# df = df[(df.relevant_comments_on_parti == 1)]
# df = df[df.if_yes.isnull()]


# df = df[['record_id', 'visit_date', 'relevant_comments_on_parti','if_yes',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/2.25 YES.xlsx')


# # # COMPLETE
# df['ea_poc_vl_enrollment_form_complete'] = df['ea_poc_vl_enrollment_form_complete'].astype('int')
# df = df[(df.ea_poc_vl_enrollment_form_complete != 2)]

# df = df[['record_id', 'visit_date', 'ea_poc_vl_enrollment_form_complete',
#          'redcap_data_access_group']].sort_values(by=['redcap_data_access_group', 'record_id'])
# df1 = df.shape
# print(df)
# print(df1)
# df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_19/COMPLETE.xlsx')