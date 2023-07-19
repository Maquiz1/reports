import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
# data = pd.DataFrame({"column1": [4, 6, 7, 1, 8]})

df = pd.read_excel(
    '/home/maquiz/Documents/DR_STELLA/DATA.xlsx', sheet_name='WBC')

df.plot(xticks=df.DAYS)
plt.show()
