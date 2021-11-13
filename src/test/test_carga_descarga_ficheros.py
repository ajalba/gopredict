from pytest_mock import MockerFixture
from gopredict.carga_descarga_ficheros import subida_archivo
import streamlit 

def test_carga_archivos_llama_file_uploader(mocker: MockerFixture):
    mocked_func=mocker.patch('streamlit.sidebar.file_uploader')
    subida_archivo('Por favor, cargue su conjunto de datos de entrenamiento')
    mocked_func.assert_called_once()