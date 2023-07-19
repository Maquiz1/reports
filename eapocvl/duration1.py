# Parental status
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date

df = pd.read_excel('~/Documents/EAPOCVL/_2023_05_07/CLIENTS.xlsx')
# df = df.columns
# print(df)

# df = df['redcap_event_name'].value_counts()
# df = df['redcap_data_access_group'].value_counts()
# df = df['what_is_the_life_status_of'].value_counts()
# df = df['redcap_event_name'].value_counts()
# print(df)


# df = df[(df['redcap_event_name'] == 'enrollment_v1_arm_1')]


df_T = df[(df['site_id'] == 1) | (df['site_id'] == 2) | (
    df['site_id'] == 3) | (df['site_id'] == 4)]

df_L = df_T[(df_T['vl'] != '')]

df_i_T = df_L[(df_L['site_id'] == 2) | (df_L['site_id'] == 4)]
df_c_T = df_L[(df_L['site_id'] == 1) | (df_L['site_id'] == 3)]

# df_L = df_L.info()

# now = datetime.now()
# now = now.strftime("%Y-%m-%d")

# def calculate_age(born):
#     today = date.today()
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# df['days_diff'] = (df.end_date-df.start_date).dt.days

# df['days_diff_from_today'] = (pd.to_datetime('today') - df_L).dt.days
# df['days_diff_from_today'] = (pd.to_datetime('today') - df_L).dt.days
# df['days_diff_from_today'] = (pd.to_datetime('today') - df_L).dt.days

# now = pd.Timestamp('now')
# dob = df_L['when_was_the_participant_f'].astype('datetime64[ns]')
# df = pd.to_datetime(df['when_was_the_participant_f'], format)    # 1

# today =  datetime.date(today)
# years = today - dob

# df['dob'] = df['dob'].where(df['dob'] < now, df['dob'] -  np.timedelta64(100, 'Y'))   # 2
# df['age'] = (now - df['dob']).astype('<m8[Y]')    # 3
# print(df)


# print(dob)


df_L = df_L['vl']
df_M = df_L.median()
df_R = df_L.max() - df_L.min()
# df.groupby("ChildID").apply(lambda x: x['abdomcirc'].max() - x['abdomcirc'].min())


df_i_T = df_i_T['vl']
df_i_M = df_i_T.median()
df_i_R = df_i_T.max() - df_i_T.min()

df_c_T = df_c_T['vl']
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
