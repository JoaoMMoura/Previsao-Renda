import streamlit as st
import pandas as pd
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("darkgrid")

st.set_page_config(
     page_title="Previsão de renda",
     page_icon="https://cdn-icons-png.flaticon.com/512/2916/2916115.png",
     layout="centered",
)
st.title('Projeto - Previsão de renda')


DATA_URL = (r"C:\Users\joao3\Documents\Jupyter Notebook - Projetos\EBAC\Módulo 16\projeto 2\input\previsao_de_renda.csv")

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)   
    return data

data_load_state = st.text('Caregando base...')
data = load_data(10000)
data_load_state.text("Base carregada!")

if st.checkbox('Exibir a base'):
    st.subheader('Base - Previsão de Renda')
    st.write(data)


st.write("Vamos plotar alguns gráficos para visualização de variáveis univariada e bivariadas")


fig, ax = plt.subplots(4,1,figsize=(10,50))
sns.boxplot(y='tempo_emprego',data=data[data['renda'] < 15000], ax=ax[0])
sns.barplot(x='educacao',y='renda',data=data, ax=ax[1])
sns.barplot(x='sexo',y='renda',data=data, ax=ax[2])
sns.barplot(x='tipo_renda',y='renda',data=data, ax=ax[3])
sns.despine()
st.pyplot(plt)
