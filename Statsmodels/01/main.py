import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dataframe = pd.read_csv('C:/Users/gabri/OneDrive/Área de Trabalho/WindowsWorkEnvironment/Python/Statsmodels/dataset.csv')

print(dataframe.head()) # obs: codigo_bairro é string
dataframe['codigo_bairro'] = dataframe['codigo_bairro'].astype('category')
dataframe['codigo_localidade'] = dataframe['codigo_localidade'].astype('category')
print()

print(dataframe.info())
print()

print(dataframe.isnull().sum())
print()

print(dataframe.describe())
print()

#sns.histplot(data = dataframe, x = 'valor_aluguel', kde = True)
#plt.show()

# Correlação entre as variáveis
print(dataframe.corr())

sns.scatterplot(data = dataframe, x = 'area_m2', y = 'valor_aluguel')
plt.show()
