import seaborn as sns
import matplotlib.pyplot as plt
from Packages.datamanage import *
import seaborn as sns

df = readfile()
filter(df)

cidade_maior_valor_office_supplies = getCidadeComMaiorVendaEmOfficeSupplies(df)

df_total_por_periodo = getTotalPeriodo(df)
df_total_por_periodo.plot(x='Data_Pedido', y='Valor_Venda', color='green')
plt.title('Total de Vendas Por Data do Pedido')
#plt.show()

df_total_venda_por_estado = getTotalPorEstado(df)
plt.figure(figsize=(16,6))
sns.barplot(
    data=df_total_venda_por_estado,
    x='Estado',
    y='Valor_Venda'
).set(title='Vendas por Estado')
plt.xticks(rotation=60)
#plt.show()

df_total_venda_por_cidade = getCidadesComMaiorVenda(df)
plt.figure(figsize=(16,6))
sns.set_palette('coolwarm')
sns.barplot(
    data=df_total_venda_por_cidade,
    x='Cidade',
    y='Valor_Venda'
).set(title='As 10 Cidades com Maior Total de Vendas')
#plt.show()

df_segmentos = getDataFrameSegmentos(df)
plt.figure(figsize=(16,6))
plt.pie(
    x=df_segmentos['Valor_Venda'],
    labels=df_segmentos['Segmento'],
    startangle=90
)

centre_circle = plt.Circle((0,0), 0.82, fc='white')
fig=plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text='Total de Vendas: ' + '$ ' + str(int(sum(df_segmentos['Valor_Venda']))), xy=(-0.25,0))
#plt.show()

df_total_por_segmento_e_periodo = getTotalPorSegmentoAno(df)

buildDescontos(df)

qtd_desconto_maior = getQtdMaioresDescontos(df)

[media_antes_desc, media_depois_desc] = getMediaAntesDepois(df)

df_media_segmento_ano = getMediaSegmentoAno(df)
plt.figure(figsize=(12,6))
sns.set()

fig1 = sns.relplot(
    kind='line',
    data=df_media_segmento_ano,
    x='Mes',
    y='Valor_Venda',
    hue='Segmento',
    col='Ano',
    col_wrap=4
)

top_subcategorias = getTopSubCategorias(df)
top_categorias = top_subcategorias.groupby('Categoria', as_index=False).sum(numeric_only=True).reset_index()

# Plot

# Listas de cores para categorias
cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']

# Listas de cores para subcategorias
cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']

# Tamanho da figura
fig, ax = plt.subplots(figsize = (18,12))

# Gráfico das categorias
p1 = ax.pie(top_categorias['Valor_Venda'], 
            radius = 1,
            labels = top_categorias['Categoria'],
            wedgeprops = dict(edgecolor = 'white'),
            colors = cores_categorias)

# Gráfico das subcategorias
p2 = ax.pie(top_subcategorias['Valor_Venda'],
            radius = 0.9,
            labels = top_subcategorias['SubCategoria'],
            colors = cores_subcategorias, 
            labeldistance = 0.7,
            wedgeprops = dict(edgecolor = 'white'), 
            pctdistance = 0.53,
            rotatelabels = True)

# Limpa o centro do círculo
centre_circle = plt.Circle((0, 0), 0.6, fc = 'white')

# Labels e anotações
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(top_subcategorias['Valor_Venda']))), xy = (-0.2, 0))
plt.title('Total de Vendas Por Categoria e Top 12 SubCategorias')
plt.show()
