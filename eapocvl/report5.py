import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('your_file.csv')
df = pd.read_excel(
    '/home/maquiz/Documents/DR_STELLA/DATA.xlsx', sheet_name='WBC')

# df.plot(x="DAYS", y=["PATIENT A", "PATIENT B", "PATIENT C"])

df.plot(x='DAYS', y='PATIENT A', kind='bar')

ax = plt.gca()
x_labels = ax.get_xticklabels()
new_labels = [df['DAYS'][int(label.get_text())-1] for label in x_labels]
ax.set_xticklabels(new_labels)

plt.show()
