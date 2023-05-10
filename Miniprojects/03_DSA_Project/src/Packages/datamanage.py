import pandas as pd
import numpy as np

def readfile():
    return pd.read_csv('C:/Users/gabri/OneDrive/Área de Trabalho/WindowsWorkEnvironment/Python/Miniprojects/03_DSA_Project/data/dataset.csv')

def filter(df:pd.DataFrame):
    df.drop_duplicates(inplace=True)
    df['Valor_Venda'] = np.array(df['Valor_Venda'], dtype=float)
    df['Valor_Venda'] = np.around(df['Valor_Venda'], decimals=2)
    df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format='%d/%m/%Y')

def getCidadeComMaiorVendaEmOfficeSupplies(df:pd.DataFrame)->pd.DataFrame:
    return (df[df['Categoria'] == 'Office Supplies'].max())['Cidade']

def getTotalPeriodo(df:pd.DataFrame)->pd.DataFrame:
    return df.groupby('Data_Pedido', as_index=False).sum(numeric_only=True)

def getTotalPorEstado(df:pd.DataFrame)->pd.DataFrame:
    return df.groupby('Estado', as_index=False).sum(numeric_only=True)

def getCidadesComMaiorVenda(df:pd.DataFrame)->pd.DataFrame:
    df_total_venda_por_cidade = df.groupby('Cidade', as_index=False).sum(numeric_only=True)
    return df_total_venda_por_cidade.sort_values('Valor_Venda', ascending=False).iloc[:10]

def getDataFrameSegmentos(df:pd.DataFrame)->pd.DataFrame:
    return df.groupby('Segmento', as_index=False).sum(numeric_only=True)

def getTotalPorSegmentoAno(df:pd.DataFrame)->pd.DataFrame:
    df['Ano'] = df['Data_Pedido'].dt.year
    df['Mes'] = df['Data_Pedido'].dt.month
    return df.groupby(['Mes', 'Ano', 'Segmento'], as_index=False).sum(numeric_only=True)

def buildDescontos(df:pd.DataFrame):
    df['Preço com Desconto'] = list(map(lambda value: value*0.85 if value>1000 else value*0.9, df['Valor_Venda']))
    df['Preço com Desconto'] = np.array(df['Preço com Desconto'], dtype=float)
    df['Preço com Desconto'] = np.around(df['Preço com Desconto'], decimals=2)

def getQtdMaioresDescontos(df:pd.DataFrame)->int:
    return list(map(lambda value: value>1000, df['Valor_Venda'])).count(True)

def getMediaAntesDepois(df:pd.DataFrame)->list:
    media_antes_desc = df['Valor_Venda'].mean()
    media_depois_desc = df['Preço com Desconto'].mean()
    return [media_antes_desc, media_depois_desc]

def getMediaSegmentoAno(df:pd.DataFrame)->pd.DataFrame:
    return df.groupby(['Mes', 'Ano', 'Segmento'], as_index=False).mean(numeric_only=True)

def getTopSubCategorias(df:pd.DataFrame)->pd.DataFrame:
    df = df.groupby(['Categoria','SubCategoria'], as_index=False).sum(numeric_only=True).sort_values('Valor_Venda', ascending=False).head(12)
    return df.sort_values('Categoria').reset_index()