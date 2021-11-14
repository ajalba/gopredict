# __main__.py
from modelo import Modelo
import streamlit as st
import pandas as pd
from carga_descarga_ficheros import subida_archivo

def main_loop():
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
            col_etiqueta = st.selectbox('Por favor, seleccione etiqueta',col_names)  
        with col3:
            test_size = st.number_input('Tamaño test',0.01,0.99,0.25,0.05)
    if(cols_atributos!=[]):
        X=modelo.realizar_particion(cols_atributos)
        y=modelo.realizar_particion(col_etiqueta)
        modelo.particion_train_test(X,y,test_size)
        modelo.entrenar()
        st.dataframe(modelo.X_train)
if __name__=="__main__":
    main_loop()