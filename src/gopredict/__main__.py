# __main__.py
from modelo import Modelo
import streamlit as st
import pandas as pd
from carga_descarga_ficheros import subida_archivo

if __name__=="__main__":
    st.sidebar.subheader('Conjunto de datos de entrenamiento')
    status, df = subida_archivo('Por favor, cargue su conjunto de datos de entrenamiento')