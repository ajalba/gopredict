#test_modelo

from assertpy import assert_that


class TestModelo:
    def test_modelo_inicia_bien( example_fixture, modelo_test):
        assert_that(modelo_test.df.to_dict()).is_equal_to({'col1': {0:1,1:2}, 'col2': {0:3,1:4}})
    def test_modelo_seleccion_atributos(example_fixture,modelo_test):
        assert_that(modelo_test.realizar_particion('col1').to_dict()).is_equal_to({0:1,1:2})