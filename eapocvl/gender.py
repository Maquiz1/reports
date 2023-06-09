
# GENDER CATEGORY
import pandas as pd


df = pd.read_excel('CLIENTS.xlsx')

dfm_f = df[(df['gender'] == 'male') | (df['gender'] == 'female')]
dfm = df[(df['gender'] == 'male')]
dff = df[(df['gender'] == 'female')]
dfm_i = dfm[(dfm['site_id'] == 2) | (dfm['site_id'] == 4)]
dff_i = dff[(dff['site_id'] == 2) | (dff['site_id'] == 4)]
dfm_c = dfm[(dfm['site_id'] == 1) | (dfm['site_id'] == 3)]
dff_c = dff[(dff['site_id'] == 1) | (dff['site_id'] == 3)]


dfm_f_T = dfm_f.shape[0]
dfm_f_P = (dfm_f_T * 100) / (dfm_f_T)


dfm_T = dfm.shape[0]
dfm_P = (dfm_T * 100) / (dfm_f_T)

dff_T = dff.shape[0]
dff_P = (dff_T * 100) / (dfm_f_T)

dfm_i_T = dfm_i.shape[0]
dfm_i_P = (dfm_i_T * 100) / (dfm_T)

dff_i_T = dff_i.shape[0]
dff_i_P = (dff_i_T * 100) / (dff_T)


dfm_c_T = dfm_c.shape[0]
dfm_c_P = (dfm_c_T * 100) / (dfm_T)

dff_c_T = dff_c.shape[0]
dff_c_P = (dff_c_T * 100) / (dff_T)

OUT PUT

print(dfm_f_T)
print(dfm_f_P)
print(dfm_T)
print(dff_T)
print(dfm_P)
print(dff_P)
print(dfm_i_T)
print(dff_i_T)
print(dfm_i_P)
print(dff_i_P)
print(dfm_c_T)
print(dff_c_T)
print(dfm_c_P)
print(dff_c_P)