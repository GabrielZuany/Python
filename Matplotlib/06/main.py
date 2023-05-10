import pandas as pd
from matplotlib import pyplot as plt
import mplcursors as mpc

plt.style.use('ggplot')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']

median_age = ages.mean()
color = '#fc4f30'

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages, bins=bins, edgecolor = 'black', alpha=0.8, log=True)
plt.axvline(median_age, color='b', label='Median age')

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

mpc.cursor(hover=2)

plt.show()