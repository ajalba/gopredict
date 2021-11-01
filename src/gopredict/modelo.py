"""
Clase para representar a los diferentes modelos y su comportamiento

atributos(de momento)
df=dataframe de entrenamiento proviniente del conjunto de datos de entrenamiento del usuario
x_train,x_test,y_train,y_test, particiones de df para entrenar el modelo

El resto de métodos son autoexplicativos
"""


class Modelo:
    #Inicializa un modelo tomando sus datos 
    def __init__(self,data):
        self.df = data
    # Devuelve una particion del dataframe
    def realizar_particion(self,cols_atributos):
        aux = self.df.copy(deep=True)
        return aux[cols_atributos]
    def entrenar():
        pass
    def predecir():
        pass
    def get_metricas_rendimiento():
        pass
