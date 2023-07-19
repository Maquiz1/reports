import pandas as pd
import numpy as np

# df = pd.read_excel('CLIENTS.xlsx')
# df = pd.read_csv('/Documents/EAPOVL/_2023_06_26/EAPOVL.csv')
# df = pd.read_excel('~/Documents/EAPOCVL/_2023_07_22/CLIENTS.xlsx')
df = pd.read_csv('/home/maquiz/Documents/EAPOVL/_2023_07_04/EAPOC.csv')

# df = pd.read_excel('/home/maquiz/Documents/EAPOVL/_2023_07_02/CLIENTS.xlsx')

# df = df.columns
# print(df)
# df = df[df.vl < 50]
# df = df[(df['redcap_event_name'] == 'screening_arm_1')]
# df = df[(df['redcap_data_access_group'] == 'amana_hospital')]
# df = df[(df['redcap_data_access_group'] == 'sinza_hospital')]
# df = df[(df['redcap_data_access_group'] == 'mwananyamala_hospi')]
# df = df[(df['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]

# INCLUSIONS
# AGE
# df = df[(df['e_1_b_volunteer_aged_at_mo'] == 1)]
# df = df[(df['e_1_a_age_in_years'] <= 24)]
# df = df[(df['e_2_documented_evidence_of'] == 1)]
# df = df[(df['e_3_receiving_art_for_trea'] == 1)]
# df = df[(df['e_3_receiving_art_for_trea'] == 1)]

# df = df[(df['e_4_has_had_a_detectable_v'] == 1)]
# df = df[(df['e_5_participant_and_legal'] == 1)]
# df = df[(df['e_3_receiving_art_for_trea'] == 1)]
# df = df[(df['e_4_has_had_a_detectable_v'] == 1)]
# df = df[(df['e_5_participant_and_legal'] == 1)]
# df = df[(df['e_6_willing_and_able_to_co'] == 1)]

# df = df[(df['f_1_any_medical_conditions'] == 2)]
# df = df[(df['f_2_already_enrolled_in_an'] == 2)]
# df = df[(df['f_3_participant_already_en'] == 2)]
# df = df[(df['f_3_participant_already_en'] == 1)]
# df = df[(df['f_4_any_medical_or_other_c'] == 1)]
# df = df['what_is_the_estimatd_dura']

# df = df[df['what_is_the_estimated_dura']]
df = df[df['what_is_the_estimatd_dura'] < '5']
# df = df[df['what_is_the_estimatd_dura'] < '5']
# df = df[['study_id', 'age', 'gender', 'marital_status',
#          'education_level', 'occupation', 'site_id', 'recent_vl', 'recent_vl_date', 'vl', 'vl_date']]
# df = df[['what_is_the_estimatd_dura']].shape
# visit_date

# df = df[df.when_was_the_sample_for_th_mon6]

# df = df[df.when_was_the_sample_for_thon6.isnull()]
# df['DateTime1'] = pd.to_datetime(df['visit_date'])

# df['DateTime2'] = pd.to_datetime(df['when_was_the_sample_for_th'])
# df['DateTime2'] = pd.to_datetime(df['when_was_the_vl_result_rec'])
# df['DateTime2'] = pd.to_datetime(df['when_was_the_vl_result_giv'])

# df['nb_months'] = ((df.DateTime1 - df.DateTime2)/np.timedelta64(1, 'M'))
# df['nb_months'] = df['nb_months'].astype(int)

# df[df['nb_months'] >= 6]

# df = df[['record_id','visit_date','nb_months','when_was_the_sample_for_th','when_was_the_vl_result_rec','when_was_the_vl_result_giv','what_is_the_most_recent_vi']].sort_values('nb_months')

df = df[['record_id','visit_date','what_is_the_estimatd_dura']].sort_values('what_is_the_estimatd_dura')

# df = df[['record_id','what_is_the_most_recent_vi_mon6']].shape
# df = df[['record_id','what_is_the_most_recent_vi_mon6']].shape
# df = df[['record_id','when_was_the_sample_for_th_mon6']]
# df = df[['record_id','is_this_the_regimen_the_pa_m_on6']]



# df = df[df.is_this_the_regimen_the_pa_m.isnull()]
# df = df[df.what_is_the_most_recent_vi_mon6.isnull()]
# df = df[df.when_was_the_vl_result_rec_mon6.isnull()]
# df = df[df.when_was_the_sample_for_th.isnull()]
# df = df[df.when_was_the_sample_for_th.isnull()]
# df = df[df.when_was_the_sample_for_th.isnull()]
# df = df[df.when_was_the_sample_for_th.isnull()]

print(df)
