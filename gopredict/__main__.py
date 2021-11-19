# __main__.py
from re import sub
from modelo import Modelo
import streamlit as st
import pandas as pd
from carga_descarga_ficheros import subida_archivo
from figuras import matriz_confusion
from figuras import curva_roc
def main_loop():
    st.sidebar.subheader('Conjunto de datos de entrenamiento')
    status, df = subida_archivo('Por favor, cargue su conjunto de datos de entrenamiento')
    modelo = Modelo(df)
    
    cols_atributos=[]
    if status == True:
        modelo.df.replace({'B':0, 'M':1}, inplace=True)
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
        modelo.predecir_entrenamiento()

        matrix_confusion = matriz_confusion(modelo.get_metricas_matriz_confusion())
        st.subheader('Matriz de Confusión')
        st.write(matrix_confusion)

        roc_data = modelo.get_metricas_roc()
        curva = curva_roc(roc_data)
        st.subheader('Curva ROC')
        st.write(curva)
        metricas =modelo.get_metricas_rendimiento()
        col2_1, col2_2, col2_3, col2_4 = st.columns(4)
        with col2_1:
            st.info('Accuracy: **%s**' % (round(metricas[0],3)))
        with col2_2:
            st.info('Precision: **%s**' % (round(metricas[1],3)))
        with col2_3:
            st.info('Recall: **%s**' % (round(metricas[2],3)))
        with col2_4:
            st.info('F1 Score: **%s**' % (round(metricas[3],3)))
    st.sidebar.subheader('Conjunto test')
    status_test, df_test = subida_archivo('Por favor suba un conjunto de datos de test')
    if status_test == True:
        st.title('Testing')
        X_test_test = df_test[cols_atributos]
        y_pred_test = modelo.prediccion_test(X_test_test)

        X_pred = df_test.copy()
        X_pred[col_etiqueta] = y_pred_test
        X_pred = X_pred.sort_index()

        st.subheader('Predicciones')
        st.write(X_pred)
        
if __name__=="__main__":
    main_loop()