# conftest.py
import pytest
import pandas as pd
from .context import gopredict
from gopredict import Modelo


@pytest.fixture(scope='class')
def modelo_test():
    datos = {'col1': [1, 2], 'col2': [3, 4]}
    df_ejemplo = pd.DataFrame(data = datos)
    return Modelo(df_ejemplo)