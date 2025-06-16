import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Painel de Indicaores públicos", 
    page_icon="🌍",
    layout="wide"

)
#Carregar os dados
df= pd.read_csv('database/indicadores.csv', sep= ',')

#Título do aplicativo
st.title('Painel de Indicadores de Governança Pública')
st.markdown("Simulação de dados públicos para auxiliar gestores na tomada de decisão.")

#Filtros 
estados = st.multiselect("Escolha os estados", df['estado']. unique(), default=df['estado'].unique())
anos = st.slider("Escolha o intervalo de anos", int(df['ano'].min()), int(df['ano'].max()),(2021,2022))

df_filtrado = df[(df['estado'].isin(estados)) & (df['ano'].between(*anos))] 

#Indicadores
col1, col1, col3 = st.columns(3)
col1.metric("ALFABETIZAÇÃO", f"{df_filtrado['alfabetizacao'].mean():.1f}%")
col2.metric("DESEMPREGO MÉDIO", f"{df_filtrado['desemprego'].mean():.1f}%")
col3.metric("Investimento em saúde", f"R${df_filtrado['investimento_saude'].mean():,.0f}mi")

#Gráfico de alfabetiação
fig1 = px.line(df_filtrado, x= 'ano', y='alfabetiacao', color='estado', markers=True, title="Evolução da Alfabetização")
st.plotly_chart(fig2, use_container_width=True)

#Gráfico de Criminalidade
fig2 =  px.bar(df_filtrado, x='estado',y=)

#Simulação de investimento
st.header("Simulação de Investimento em Saúde")
incremento = st.slider("Aumentar o investimento em Saúde (%)", 0, 100, 10)
df_simulado = df_filtrado.copy()
df_simulado['investimento_saude'] *= (1 + incremento / 100)

st.dataframe(df_simulado[['estado', 'ano', 'investimento_saude_milhoes']])

#Exportar CSV
csv = df_simulado.to_csv(index= False). encode('utf-8')
st.download_button(
    label="Dowload CSV",
    data=csv,
    file_name='simulacao_investimento.csv',
    mime='text/csv',
)


