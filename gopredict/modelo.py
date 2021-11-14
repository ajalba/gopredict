"""
Clase para representar a los diferentes modelos y su comportamiento

atributos(de momento)
df=dataframe de entrenamiento proviniente del conjunto de datos de entrenamiento del usuario
x_train,x_test,y_train,y_test, particiones de df para entrenar el modelo

El resto de métodos son autoexplicativos
"""


from numpy import array
from pandas.core.frame import DataFrame
from sklearn.model_selection import train_test_split

class Modelo:
    #Inicializa un modelo tomando sus datos 
    def __init__(self,data):
        self.df = data
        self.X_train = None
        self.X_test  = None
        self.y_train = None
        self.y_test  = None
        self.modelo=None
    # Devuelve una particion del dataframe
    def realizar_particion(self,cols_atributos:array):
        aux = self.df.copy(deep=True)
        return aux[cols_atributos]
    #Realiza una particion en train y test
    def particion_train_test(self,X:DataFrame, y:DataFrame, test_porcentaje:int):
        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(
            X,y,test_size=test_porcentaje,random_state=0)

    def entrenar():
        pass
    def predecir():
        pass
    def get_metricas_rendimiento():
        pass
