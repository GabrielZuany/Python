import pandas as pd
from diretivas_de_compilacao import *


def RemoveUnamedColumns(data_df:pd.DataFrame):
    out = pd.DataFrame()
    out = data_df.loc[:, ~data_df.columns.str.contains(UNNAMED)]
    return out


def GenVendaRelativa(data_df:pd.DataFrame, campo_1:str, campo_2:str, x:int):
    return round((data_df[campo_1] / data_df[campo_2]),2)


def GetFullColumnItem(data_df:pd.DataFrame, column_name:str, value_name:str):
    df = data_df.loc[data_df[column_name] == value_name]
    return df


def RemoveColumn(data_df:pd.DataFrame, namespace:str):
    out = data_df.loc[:, ~data_df.columns.str.contains(namespace)]
    return out


def GeraRelatorioFuncionario(data_df:pd.DataFrame, loja: str):
    Loja_df_funcionarios =  data_df.sort_values(by=TOTAL_VENDA_PRODUTOS_DO_FUNCIONARIO, ascending=False)

    Loja_df_funcionarios = RemoveColumn(Loja_df_funcionarios, OUTRAS_INFORMACOES)
    Loja_df_funcionarios = RemoveColumn(Loja_df_funcionarios, PRECO_PRODUTO)
    Loja_df_funcionarios = RemoveColumn(Loja_df_funcionarios, PRODUTO)
    
    Loja_df_funcionarios[MEDIA_VALOR_X_QTD_VENDIDA] = GenVendaRelativa(data_df, TOTAL_VENDA_PRODUTOS_DO_FUNCIONARIO, QTD_VENDA_PRODUTOS_FUNCIONARIO, 2)
    
    return Loja_df_funcionarios


def GenRelatorioLojasIndividual(filepath_mes_atual:str, data_df:pd.DataFrame, column_name:str, item_name:str):
    
    Loja_df = GetFullColumnItem(data_df, column_name, item_name)
    Loja_df_geral = Loja_df.describe()
    Loja_df_geral = RemoveColumn(Loja_df_geral, ID_FUNCIONARIO)
    Loja_df_geral = RemoveColumn(Loja_df_geral, ID_LOJA)
    Loja_df_geral = Loja_df_geral.drop(labels='count')
    
    Loja_df_funcionarios =  GeraRelatorioFuncionario(Loja_df, item_name)
    
    with pd.ExcelWriter(filepath_mes_atual) as writer:
        Loja_df_geral.to_excel(writer, sheet_name=SHEET_GERAL)
        Loja_df_funcionarios.to_excel(writer, sheet_name=SHEET_FUNCIONARIOS, index=False)  
        
        
def GeraRelatorioLojas(data_df: pd.DataFrame):
    
    data_df = data_df.groupby(by = [CAMPO_LOJA], group_keys=True, observed=True).sum(numeric_only=True)
    data_df[MEDIA_VALOR_X_QTD_VENDIDA] = GenVendaRelativa(data_df, TOTAL_VENDA_PRODUTOS_DO_FUNCIONARIO, QTD_VENDA_PRODUTOS_FUNCIONARIO, 2)
    data_df = RemoveColumn(data_df, ID_FUNCIONARIO)
    data_df = RemoveColumn(data_df, PRECO_PRODUTO)
    data_df = RemoveColumn(data_df, ID_LOJA)
    
    return data_df


def GeraRelatorioTodasAsLojas(data_df:pd.DataFrame):
    for loja in data_df[CAMPO_LOJA]:
        nome = PATH_OUT + loja + ".xlsx"
        GenRelatorioLojasIndividual(nome, data_df, CAMPO_LOJA, loja)


def GeraRankingLojas(data_df: pd.DataFrame):
    return data_df.sort_values(by=TOTAL_VENDA_PRODUTOS_DO_FUNCIONARIO, ascending=False)