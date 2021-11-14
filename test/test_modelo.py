#test_modelo

from assertpy import assert_that


class TestModelo:
    def test_modelo_inicia_bien(self, modelo_test):
        assert_that(modelo_test.df.to_dict()).is_equal_to({'col1': {0:1,1:2,2:3}, 
        'col2': {0:0,1:1,2:1},
        'col3':{0:1,1:0,2:1}})
        
    
    def test_modelo_seleccion_atributos(self,modelo_test):
        assert_that(modelo_test.realizar_particion('col1').to_dict()).is_equal_to({0:1,1:2,2:3})
    
    def test_modelo_train_test_split(self,modelo_test):
        assert_that(modelo_test.particion_train_test(modelo_test.realizar_particion(['col1','col2'])
        ,modelo_test.realizar_particion('col3'),0.2)).is_true()
    
    def test_modelo_entrenamiento(self, modelo_test):
        assert_that(modelo_test.entrenar()).is_true()
   
    def test_modelo_predecir_entrenamiento(self, modelo_test):
        assert_that(modelo_test.predecir_entrenamiento()).is_true()

    def test_modelo_metricas_rendimiento(self, modelo_test):
        assert_that(modelo_test.get_metricas_rendimiento()).is_iterable

    def test_modelo_metricas_matriz_confusion(self, modelo_test):
        assert_that(modelo_test.get_metricas_matriz_confusion()).is_iterable
    
  
  