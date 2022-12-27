from asyncio.windows_events import NULL
import pandas as pd

#dataframe = pd.DataFrame()
values = {
    'data': ['10/02/2022', '26/12/2022'],
    'valor': [500, 300],
    'produto': ['feijao', 'arroz'],
    'qtde': [50, 60]
}

#vendas_df = pd.DataFrame(values)

vendas_df = pd.read_excel("01_Pandas\prod.xlsx")

#imprime a tabela completa
print(vendas_df) 

#print(vendas_df.head(1)) #vendas_df.head(numero de linhas que deseja ver)

#mostra as proporções da tabela -> evita o custo de imprimir a tabela inteira
#print(vendas_df.shape) 

#impirme as informações do desvio padrao, maximos e minimos, quartis...
#print(vendas_df.describe()) 

valores_numericos = vendas_df[['valor', 'qtd']]
#print(valores_numericos)

print() 

#imprime a linha do indice dado.
#print(vendas_df.loc[0]) 

#vendas_df.loc[linhas, colunas]
#print(vendas_df.loc[vendas_df['produto'] == 'teste'] , ["data", 'qtd']) 
print()

#criar nova coluna
vendas_df['Comissao'] = vendas_df["valor"] * 0.05 

#criar nova coluna
vendas_df.loc[:, 'Imposto'] = NULL 
#print(vendas_df)
print()

#deletar linhas e colunas completamente vazias
#vendas_df = vendas_df.dropna(how='all', axis = 1) # axis = 1: linha, = 0: coluna

#deletar linhas e/ou colunas com pelo meno um valor vazio
vendas_df = vendas_df.dropna()

#preencher valores vazios
#vendas_df['Coluna'] = vendas_df['Coluna'].fillna(valor)

#frequencia de um determiando item da tabela
frequencia = vendas_df['produto'].value_counts()
#print(frequencia)

#agrupar e manipular
valor_final = vendas_df.groupby('produto').sum('valor')
print(valor_final)
