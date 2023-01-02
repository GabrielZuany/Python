import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from mplcursors import cursor

#Relação entre o valor atual das dívidas das famílias com o Sistema Financeiro Nacional e a renda das famílias acumulada nos últimos doze meses.
# Logo: v > 1 indica que a familia deve mais que recebe
# v = 1 indica que ta no 0 a 0
# v < 1 indica que a familia deve menos do que acumulou nos ultimos doze meses

plt.style.use('ggplot')

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.29037/dados?formato=csv"
response = requests.get(url)

csv_text = response.text
print(csv_text)

full_data = pd.read_csv(StringIO(csv_text), sep=';')

dates = pd.to_datetime(full_data['data'])
values = []

for v in full_data["valor"]:
    v = str(v).replace(",", ".")
    v = float(v)
    values.append(v)


bins = np.arange(start = 0, stop=max(values) ,step=5, dtype= float)
plt.hist(values ,bins=bins, label='Endividamento das familias', edgecolor='black', alpha=0.75)

plt.title('Endividamento das familias com\no Sistema Financeiro Nacional')
plt.xlabel('Divida / Renda')
plt.ylabel('Numero de familias endividadas')

plt.tight_layout()
cursor(hover=2)

plt.show()