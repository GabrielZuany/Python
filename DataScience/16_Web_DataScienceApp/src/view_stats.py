import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
from diretivas_de_compilacao import *

BARCOLOR = "#FF4B4B"

@st.cache
def OpenFile_Relatorio():
    data = pd.read_excel(PATH_OUT+RELATORIO_FILENAME)
    return data


def Lojas_Layout(data:pd.DataFrame):
    st.title(body="Análise de Dados Monnera")
    st.markdown("---")
    sidebar = st.sidebar.header("Monnera")
    sidebar = st.sidebar.markdown("---")
    
    container = st.container()
    
    with container:
        [x, y, sidebar] = Seletor_Eixos(data, sidebar)
        
        [ordenacao, sidebar] = Seletor_Ordenacao(sidebar)
        
        Lojas_Subplots("", data, x, y, ordenacao, 'v')
        
        # ---- HIDE STREAMLIT STYLE ----
        hide_st_style = """
                    <style>
                    #MainMenu {visibility: show;}
                    footer {visibility: show;}
                    header {visibility: show;}
                    </style>
                    """
        st.markdown(hide_st_style, unsafe_allow_html=True)
        
        with st.expander("See explanation"):
            st.write("Explicar dados. Conclusoes/Inferencias estatisticas")
    

def Seletor_Eixos(data, sidebar):
    lojas = data[CAMPO_LOJA]
    qtd_vendas_cd_loja = data[QTD_VENDA_PRODUTOS_FUNCIONARIO]
    total_vendas_cd_loja = data[TOTAL_VENDA_PRODUTOS_DO_FUNCIONARIO]
    media_por_venda_cd_loja = data[MEDIA_VALOR_X_QTD_VENDIDA]
    x=lojas
    y=total_vendas_cd_loja
    
    op = st.sidebar.selectbox('Relação', ('Total de vendas', 'Quantidade de vendas', 'Rendimento lojas'))
    sidebar = st.sidebar.markdown('---')
    
    if(op=='Total de vendas'):
        x = lojas
        y = total_vendas_cd_loja
    elif(op=='Quantidade de vendas'):
        x = lojas
        y = qtd_vendas_cd_loja
    elif(op=='Rendimento lojas'):
        x = lojas
        y = media_por_venda_cd_loja
        
    return [x, y, sidebar]
    
    
def Seletor_Ordenacao(sidebar):
    ordenacao = st.sidebar.radio(
        "Ordenação",
        options=["Não Ordenado", "Ascendente", "Descendente"],
    )
    if ordenacao=="Ascendente":
        ordenacao=True
    elif ordenacao=="Descendente":
        ordenacao=False
    else:
        ordenacao=None
    
    return [ordenacao, sidebar]
       
        
def Lojas_Subplots(label:str, data:pd.DataFrame, x:pd.Series, y:pd.Series, ascending:bool|None, orientation:str):
    
    if(ascending != None):
        y=y.sort_values(ascending=ascending)
        
    lojas_relatorio = px.bar(
        data_frame = data,
        x=x,
        y=y,
        orientation=orientation,
        title=f"<b>{label}</b>",
        color_discrete_sequence=[BARCOLOR] * len(y)*len(x),
        template="plotly_white",
        opacity=0.75,
        labels=dict(x=x.name, y=y.name),
    )
    
    lojas_relatorio.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
    )
    st.plotly_chart(lojas_relatorio, use_container_width=False)
 

def BuildWebApp():
    data = OpenFile_Relatorio()
    Lojas_Layout(data)
    
    st.markdown("---")
    
    st.dataframe(data, use_container_width=True)
    st.download_button('Download', data="csv", file_name='large_df.csv')
    
    
    st.markdown('---')
    
    return