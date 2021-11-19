import streamlit as st
import pandas as pd
import base64

"""
Destinado a la carga y descarga de ficheros dentro de la aplicación

"""

"""
Toma un archivo en formato csv y devuelve un dataframe que se ha hecho con él
"""

def subida_archivo(display):
    uploaded_file = st.sidebar.file_uploader('%s' % (display),key='%s' % (display),accept_multiple_files=False)
    content = False
    if uploaded_file is not None:
        try:
            uploaded_df = pd.read_csv(uploaded_file)
            content = True
            return content, uploaded_df
        except:
            try:
                uploaded_df = pd.read_excel(uploaded_file)
                content = True
                return content, uploaded_df
            except:
                st.error('Los formatos admitidos son .csv y .xlsx, por favor, inténtelo de nuevo.')
                return content, None
    else:
        return content, None


"""
Toma un data frame y un nombre para el archivo y devuelve un enlace para descargar dicho dataframe
en formato csv
"""
def descarga_archivo(df,nombre_archivo):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = (f'<a href="data:file/csv;base64,{b64}" download="%s.csv">Download csv file</a>' % (nombre_archivo))
    return href