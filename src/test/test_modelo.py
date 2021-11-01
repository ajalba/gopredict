#test_modelo
from assertpy import assert_that
from .context import gopredict

class TestModelo:
    def test_modelo_inicia_bien( example_fixture):
        modelo = gopredict.Modelo(1)
        assert_that(modelo.dato).is_equal_to(1)
    def test_modelo_patata(example_fixture):
        assert_that(1).is_equal_to(2)