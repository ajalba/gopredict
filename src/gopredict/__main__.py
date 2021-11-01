# __main__.py
from modelo import Modelo
import streamlit as st
import pandas as pd
from carga_descarga_ficheros import subida_archivo

if __name__=="__main__":
    st.sidebar.subheader('Conjunto de datos de entrenamiento')
    status, df = subida_archivo('Por favor, cargue su conjunto de datos de entrenamiento')
    modelo = Modelo(df)
    cols_atributos=[]
    if status == True:
        col_names = list(df)
        
        st.title('Entrenamiento')
        st.subheader('Parámetros')
        col1, col2, col3 = st.columns((3,3,2))

        with col1:
            cols_atributos = st.multiselect('Por favor, seleccione atributos',col_names)
        with col2:
            label_col = st.selectbox('Por favor, seleccione etiqueta',col_names)  
    if(cols_atributos!=[]):
        df_reducido=modelo.realizar_particion(cols_atributos)