# Adding a Y-Axis Label to
# the Secondary Y-Axis in Matplotlib
# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df = pd.read_excel(
#     '/home/maquiz/Documents/DR_STELLA/DATA.xlsx', index_col='DAYS', sheet_name='WBC')
df = pd.read_excel(
    '/home/maquiz/Documents/DR_STELLA/DATA.xlsx', sheet_name='WBC')

# plt.plot(x, y)
# df.plot(x="DAYS", y=["PATIENT A", "PATIENT B", "PATIENT C"],
#         kind="line", , fontsize=4)
df.plot(x="DAYS", y=["PATIENT A", "PATIENT B", "PATIENT C"], rot=0)

# ax = plt.gca()
# x_labels = ax.get_xticklabels()

# new_labels = [df['DAYS'][int(label.get_text())-1] for label in x_labels]
# ax.set_xticklabels(new_labels)


plt.ylabel('WBC')
plt.xlabel('DAYS')
plt.title("PROGRESS FBP OF WBC")
# plt.xticks(np.arange(0, 100, 2))
# plt.xticks(df.DAYS)
plt.yticks(np.arange(0, 25, 2))

# print(x_labels)

plt.show()