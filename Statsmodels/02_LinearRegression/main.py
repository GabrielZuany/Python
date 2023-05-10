import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Regressão linear simples
# Y = a + bX + e, em que Y = valor_aluguel e X = area_m2 e e = erro aleatório. 
# a e b são os parâmetros a serem estimados pelo modelo de regressão linear simples (OLS).

dataframe = pd.read_csv('C:/Users/gabri/OneDrive/Área de Trabalho/WindowsWorkEnvironment/Python/Statsmodels/dataset.csv')

print(dataframe.head())

y = dataframe['valor_aluguel'] # variável dependente
x = dataframe['area_m2'] # variável independente
x = sm.add_constant(x) # adiciona uma constante (a) à regressão linear simples
model = sm.OLS(y, x) # cria o modelo de regressão linear simples
result = model.fit() # treina o modelo

print(result.summary())

plt.figure(figsize = (12, 6))
plt.xlabel('Área (m²)')
plt.ylabel('Valor do aluguel (R$)')
plt.plot(x['area_m2'], y, 'o', label = 'Dados Reais')
plt.plot(x['area_m2'], result.predict(), 'r-', label = 'Regressão Linear Simples')
plt.legend(loc = 'best')
plt.show()