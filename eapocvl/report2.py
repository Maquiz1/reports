# Adding a Y-Axis Label to
# the Secondary Y-Axis in Matplotlib
# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# creating dataframe for plot
# dataset = pd.DataFrame({'Name': ['Rohit', 'Seema',
#                                  'Meena', 'Geeta',
#                                  'Rajat'],

#                         'Height': [155, 129, 138, 164, 145],
#                         # 'Weight': [60, 40, 45, 55, 60]})
#                         'Height2': [160, 139, 128, 154, 135]})

df = pd.read_excel(
    '/home/maquiz/Documents/DR_STELLA/DATA.xlsx', index_col='DAY')

# plt.plot(x, y)
df.plot()
plt.ylabel('PATIENTS')
plt.xlabel('DAYS')
plt.title("PROGRESS FBP")
plt.xticks(np.arange(0, 62, 2))
plt.yticks(np.arange(0, 550, 50))


plt.show()

