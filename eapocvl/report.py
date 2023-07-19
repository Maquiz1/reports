import pandas as pd
import matplotlib.pyplot as plt



# df = pd.read_excel('CLIENTS.xlsx')
# df = pd.read_csv('/Documents/EAPOVL/_2023_06_26/EAPOVL.csv')
# df = pd.read_excel('~/Documents/EAPOCVL/_2023_07_22/CLIENTS.xlsx')
# df = pd.read_csv('/home/maquiz/Documents/DR_STELLA/_2023_07_02/EAPOC.csv')

# df = pd.read_excel('/home/maquiz/Documents/DR_STELLA/DATA.xlsx',
#                    index_col=0, parse_dates=True)

df = pd.read_excel('/home/maquiz/Documents/DR_STELLA/DATA.xlsx')

# df.plot(y='DAY', kind='line')
df.plot()

plt.show()

# df = pd.DataFrame(np.random.randn(
#     1000, 4), index=ts.index, columns=list("ABCD"))
# df = pd.DataFrame(df,columns=list("wbc"))

# df = df.cumsum()

# df.figure()



# df.plot()



# df = df.columns
# print(df)
# df = df[df.vl < 50]
# df = df[(df['redcap_event_name'] == 'screening_arm_1')]
# df = df[(df['redcap_data_access_group'] == 'mwananyamala_hospi')]


# # INCLUSIONS
# # AGE
# df = df[(df['e_1_b_volunteer_aged_at_mo'] == 1)]
# df = df[(df['e_1_a_age_in_years'] <= 24)]
# df = df[(df['e_2_documented_evidence_of'] == 1)]
# df = df[(df['e_3_receiving_art_for_trea'] == 1)]
# df = df[(df['e_3_receiving_art_for_trea'] == 1)]
# df = df[(df['e_4_has_had_a_detectable_v'] == 1)]
# df = df[(df['e_5_participant_and_legal'] == 1)]
# df = df.e_5_participant_and_legal.isna
# # df = df[(df['e_3_receiving_art_for_trea'] == 1)]








# df = df[['study_id', 'age', 'gender', 'marital_status',
#          'education_level', 'occupation', 'site_id', 'recent_vl', 'recent_vl_date', 'vl', 'vl_date']]


# AGE CATEGORY
# dfm_f = df[(df['age'] == 'male') | (df['age'] == 'female')]
# dfm = df[(df['gender'] == 'male')]
# dff = df[(df['gender'] == 'female')]
# dfm_i = dfm[(dfm['site_id'] == 2) | (dfm['site_id'] == 4)]
# dff_i = dff[(dff['site_id'] == 2) | (dff['site_id'] == 4)]
# dfm_c = dfm[(dfm['site_id'] == 1) | (dfm['site_id'] == 3)]
# dff_c = dff[(dff['site_id'] == 1) | (dff['site_id'] == 3)]


# dfm_f_T = dfm_f.shape[0]
# dfm_f_P = (dfm_f_T * 100) / (dfm_f_T)


# dfm_T = dfm.shape[0]
# dfm_P = (dfm_T * 100) / (dfm_f_T)

# dff_T = dff.shape[0]
# dff_P = (dff_T * 100) / (dfm_f_T)

# dfm_i_T = dfm_i.shape[0]
# dfm_i_P = (dfm_i_T * 100) / (dfm_T)

# dff_i_T = dff_i.shape[0]
# dff_i_P = (dff_i_T * 100) / (dff_T)


# dfm_c_T = dfm_c.shape[0]
# dfm_c_P = (dfm_c_T * 100) / (dfm_T)

# dff_c_T = dff_c.shape[0]
# dff_c_P = (dff_c_T * 100) / (dff_T)

print(df)
