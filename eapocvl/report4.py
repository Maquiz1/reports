import pandas as pd
import matplotlib.pyplot as plt

data = {'Column1': [1, 2, 3, 4, 5],
        'Column2': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

df.plot(x='Column1', y='Column2', kind='bar')

ax = plt.gca()
x_labels = ax.get_xticklabels()
new_labels = [df['Column1'][int(label.get_text())-1] for label in x_labels]
ax.set_xticklabels(new_labels)

plt.show()
