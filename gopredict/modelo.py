"""
Clase para representar a los diferentes modelos y su comportamiento

atributos(de momento)
df=dataframe de entrenamiento proviniente del conjunto de datos de entrenamiento del usuario
x_train,x_test,y_train,y_test, particiones de df para entrenar el modelo

El resto de métodos son autoexplicativos
"""


from numpy import array
from pandas.core.frame import DataFrame
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

class Modelo:
    #Inicializa un modelo tomando sus datos 
    def __init__(self,data):
        self.df = data
        self.X_train = None
        self.X_test  = None
        self.y_train = None
        self.y_test  = None
        self.y_pred  = None
        self.modelo=LogisticRegression()
    # Devuelve una particion del dataframe
    def realizar_particion(self,cols_atributos:array):
        aux = self.df.copy(deep=True)
        return aux[cols_atributos]
    #Realiza una particion en train y test
    def particion_train_test(self,X:DataFrame, y:DataFrame, test_porcentaje:int):
        try:
            self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(
                X,y,test_size=test_porcentaje,random_state=0)
            return True
        except:
            return False
    #Entrena el modelo con los datos de entrenamiento
    def entrenar(self):
        try:
            self.modelo.fit(self.X_train, self.y_train)
            return True
        except Exception as e:
            print(e)
            return False
    #Realiza una prediccion sobre el conjunto de entrenamiento
    def predecir_entrenamiento(self):
        try:
            self.y_pred = self.modelo.predict(self.X_test)
            return True
        except:
            return False

    #devuelve las métricas de rendimiento del modelo en entrenamiento
    def get_metricas_rendimiento(self):
        accuracy = metrics.accuracy_score(self.y_test, self.y_pred)
        precision = metrics.precision_score(self.y_test, self.y_pred, zero_division=0)
        recall = metrics.recall_score(self.y_test, self.y_pred)
        f1 = metrics.f1_score(self.y_test, self.y_pred)
        return [accuracy,precision,recall,f1]

    #Devuelve las métricas para la matriz de confusion
    def get_metricas_matriz_confusion(self):
        return metrics.confusion_matrix(self.y_test,self.y_pred)

    def get_metricas_roc(self):
        y_pred_proba = self.modelo.predict_proba(self.X_test)[::,1]
        fpr, tpr, _ = metrics.roc_curve(self.y_test,  y_pred_proba)
        fpr, tpr, _ = metrics.roc_curve(self.y_test,  y_pred_proba)
        roc_data = pd.DataFrame([])
        roc_data['True Positive'] =  tpr
        roc_data['False Positive'] = fpr
        return roc_data
    def prediccion_test(self,X_test_test):
        y_pred_test=self.modelo.predict(X_test_test)
        return y_pred_test

