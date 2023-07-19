import pandas as pd
import numpy as np

# df = pd.read_excel('CLIENTS.xlsx')
# df = pd.read_csv('/Documents/EAPOVL/_2023_06_26/EAPOVL.csv')
# df = pd.read_excel('~/Documents/EAPOCVL/_2023_07_22/CLIENTS.xlsx')
df = pd.read_csv('/home/maquiz/Documents/EAPOVL/_2023_07_17/EAPOC.csv')

# df = pd.read_excel('/home/maquiz/Documents/EAPOVL/_2023_07_02/CLIENTS.xlsx')

# df = df.columns
# print(df)
# df = df[df.vl < 50]
# df = df[(df['redcap_event_name'] == 'screening_arm_1')]
df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]
df = df[(df['redcap_data_access_group'] == 'amana_hospital') | (df['redcap_data_access_group'] == 'sinza_hospital') | (
    df['redcap_data_access_group'] == 'mwananyamala_hospi') | (df['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]
# df = df[(df['redcap_data_access_group'] == 'amana_hospital')]
# df = df[(df['redcap_data_access_group'] == 'sinza_hospital')]
# df = df[(df['redcap_data_access_group'] == 'mwananyamala_hospi')]
# df = df[(df['redcap_data_access_group'] == 'mnazi_mmoja_hospit')]


# INCLUSIONS
# df = df[(df['d_visit_date'] == '')]
# df = df[(df['e_1_b_volunteer_aged_at_mo'] == 1)]
# df = df[(df['e_1_a_age_in_years'] <= 24)]
# df = df[(df['e_2_documented_evidence_of'] != 1)]
# df = df[(df['e_3_receiving_art_for_trea'] != 1)]
# df = df[(df['e_4_has_had_a_detectable_v'] != 1)]
# df = df[(df['e_5_participant_and_legal'] != 1)]
# df = df[(df['e_6_willing_and_able_to_co'] != 1)]


# EXCLUSIONS
# df = df[(df['f_1_any_medical_conditions'] != 2)]
# df = df[(df['f_2_already_enrolled_in_an'] != 2)]
# df = df[(df['f_3_participant_already_en'] != 2)]
# df = df[(df['f_4_any_medical_or_other_c'] != 2)]
# df = df[(df['g_is_the_volunteer_eligibl'] != 1)]
# df = df[(df['i_if_eligible_enter_study'] == '')]


# ENROLLMENT
# df = df[(df['participant_initials'] == '')]
# df = df[(df['participant_id'] == '')]
# df = df[(df['visit_date'] == '')]
# df = df[(df['is_the_participant_eligibl_1'] != 1)]
# df = df[(df['has_written_consent_assent'] != 1)]
# df = df[(df['date_of_informed_consent'] == '')]
# df = df[(df['participant_s_gender'] == '')]
# df = df[(df['participant_s_country_of_o'] == '')]
# df = df[(df['participant_s_ethnicity'] == '')]
# df = df[(df['which_art_regimen_is_the_p'] == '')]

# df = df[(df['how_long_has_the_participa'] == '')]
# df = df[(df['how_long_has_the_participa'] < 6)]
# df = df[(df['is_this_the_regimen_the_pa'] == '')]
# df = df[(df['what_is_the_most_recent_vi'] == '')]
# df = df[(df['when_was_the_sample_for_th'] == '')]
# df = df[(df['when_was_the_vl_result_rec'] == '')]
# df = df[(df['when_was_the_vl_result_giv'] == '')]
# df = df[(df['what_is_the_participant_s'] == '')]
# df = df[(df['a_check_most_recent_result'] == '')]
# df = df[df.a_check_most_recent_result.isnull()]
# df = df[df.height.isnull()]
# df = df[df.weight.isnull()]
# df = df[df.systolic_blood_pressure.isnull()]
# df = df[df.diastolic_blood_pressure.isnull()]
# df = df[df.which_art_regimen_is_the_p.isnull()]


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
df = df[['record_id', 'visit_date', 'when_did_the_participant_s', 'redcap_data_access_group']
        ].sort_values('redcap_data_access_group')

# df = df[['record_id', 'visit_date', 'when_did_the_participant_s','nb_months', 'redcap_data_access_group']
#         ].sort_values('redcap_data_access_group')

# df = df[['record_id', 'visit_date', 'when_was_the_sample_for_th','what_is_the_most_recent_vi','nb_months', 'redcap_data_access_group']
#         ].sort_values(by=['redcap_data_access_group', 'nb_months'])

df1 = df.shape
print(df)
print(df1)
df.to_excel('/home/maquiz/Documents/EAPOVL/_2023_07_17/RECENT VIRAL LOAD DATE MISSING.xlsx')

