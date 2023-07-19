import pandas as pd


# df = pd.read_excel('CLIENTS.xlsx')
df = pd.read_csv('/home/maquiz/Documents/EAPOVL/_2023_07_02/EAPOC.csv')

# df = df.columns
# print(df)
# df = df[df.vl < 50]
# df = df[(df['redcap_event_name'] == 'screening_arm_1')]
df = df[(df['redcap_data_access_group'] == 'mwananyamala_hospi')]
# df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]


# df = df['what_is_the_estimatd_dura']
df = df[df.when_did_the_participant_s.isnull()]
# df = df[df['what_is_the_estimatd_dura'] <= 5]

# df = df[['record_id','when_did_the_participant_s','what_is_the_estimatd_dura']]
# df = df[['record_id', 'when_did_the_participant_s', 'what_is_the_estimatd_dura']]


print(df)
