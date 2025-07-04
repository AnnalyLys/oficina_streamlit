import streamlit as st
import pandas as pd


#Configuração da página
st.title("Pré Carteira Nacional Digital")


    #entrada de idade
idade = st.number_input("Informe sua idade:", min_value=0, step=1)


    #verificação da idade
if idade >= 18:
    
    st.success("Você pode continuar a fazer sua carteira pelo site.")
    st.ballons()
    st.snow()
    
    #Botão com link para o site oficial da CNH
    st.markdown("[Clique aqui para acessar o site da CNH](https://www.gov.br/pt-br/temas/carteira-nacional-de-habilitacao-cnh)", unsafe_allow_html=True)
else:
    input("Ops! Você não tem idade o suficiente para fazer a CNH. Tente novamente assim que completar 18 anos")
    
   
 
