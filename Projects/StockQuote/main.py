from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

tabela_empresas = pd.read_excel("Empresas.xlsx")

for empresa in tabela_empresas['Empresas']:
    Cot = web.DataReader(f'{empresa}.SA', data_source='yahoo', start='01/01/2020', end='01/01/2021')#ticker, data_source, start/end='Month/day/year'
    display(Cot)
    Cot["Adj Close"].plot()
    plt.show()#Show Adj close graphic.