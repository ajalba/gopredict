from pytest_mock import MockerFixture
from gopredict.__main__ import main_loop


def test_main_llama_subida_archivo(mocker: MockerFixture):
    mocked_func=mocker.patch('gopredict.carga_descarga_ficheros.subida_archivo')
    mock_loop = mocker.patch('gopredict.__main__.main_loop')
    main_loop()
    mocked_func.assert_any_call
    

def test_main_llama_subheader(mocker: MockerFixture):
    mocked_func=mocker.patch('streamlit.sidebar.subheader')
    main_loop()
    mocked_func.assert_called_once()



    
   