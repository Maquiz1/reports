import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    '/home/maquiz/Documents/DR_STELLA/DATA.xlsx', sheet_name='WBC')

# df = pd.DataFrame(df)
plt.figure(figsize=(60, 6))
df.plot(x='DAYS',y=['PATIENT A','PATIENT B','PATIENT C'], figsize=(15,6), title='PROGRESS FBP OF WBC', ylabel='WBC')

plt.show()
