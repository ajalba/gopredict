# conftest.py
import pytest
import pandas as pd
from gopredict.modelo import Modelo
import numpy as np
@pytest.fixture(scope='class')
def modelo_test():
    datos = {'col1': [1, 2,3], 'col2': [0, 1,1],'col3':[1,0,1]}
    df_ejemplo = pd.DataFrame(data = datos)
    return Modelo(df_ejemplo)

@pytest.fixture(scope='function')
def data_test_roc():
    datos = {'False Positive': [1, 1], 'True Positive': [0, 1]}
    return pd.DataFrame(data = datos) 

@pytest.fixture(scope='function')
def data_test_matriz_confusion():
    datos = np.array([[0,1],[0,0]])
    return datos   

