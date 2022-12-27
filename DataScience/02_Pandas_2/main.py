import pandas as pd
import managedata as md
from diretivas_de_compilacao import *
import seaborn as sns
import matplotlib.pyplot as plt
import os

try:
    os.mkdir(PATH_OUT)
except:
    print("Pasta ja existente. Contiunuando a execucao")
    
full_df = pd.read_excel(PATH_IN + FULL_DF_IN)
full_df[TOTAL_VENDA_PRODUTOS_DO_FUNCIONARIO] = full_df[QTD_VENDA_PRODUTOS_FUNCIONARIO] * full_df[PRECO_PRODUTO]
full_df.to_excel(PATH_IN + FULL_DF_IN, index=False)

allow_to_modify_df = md.RemoveUnamedColumns(full_df)

md.GeraRelatorioTodasAsLojas(allow_to_modify_df)

relatorio_df = md.GeraRelatorioLojas(allow_to_modify_df)
ranking_df = md.GeraRankingLojas(relatorio_df)

relatorio_df.to_excel(PATH_OUT + RELATORIO_FILENAME, index=True)
ranking_df.to_excel(PATH_OUT + RANKING_FILENAME, index=True)

gr = sns.lmplot(data=relatorio_df, x=PRECO_PRODUTO, y=QTD_VENDA_PRODUTOS_FUNCIONARIO)
plt.show()