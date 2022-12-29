import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

data = pd.read_csv('data.csv')
ages = data['Age']
all_dev_salary = data['All_Devs']
py_salary = data['Python']
js_salary = data['JavaScript']

overwall_mean = 57252

ages = np.array(ages, dtype=int)
py_salary = np.array(py_salary, dtype=int)
js_salary = np.array(js_salary, dtype=int)

plt.fill_between(ages, py_salary, js_salary, color='b', label = 'Above Avg', alpha=.25, linewidth=0.2, where=(py_salary>js_salary), interpolate=True) # fill when the line cross the overwall value
plt.fill_between(ages, py_salary, js_salary, label = 'Below Avg', alpha=.25, linewidth=0.2, where=(py_salary<=js_salary), interpolate=True) # fill before the line cross the overwall value

plt.plot(ages, py_salary, label='Python', color='b', linewidth=1, alpha=.75)

plt.plot(ages, js_salary, label='JS Devs', linestyle='--', color='grey', linewidth=1)

plt.xlabel('Age')
plt.ylabel('Medium Salary (USD)')
plt.legend()
plt.tight_layout()

plt.show()