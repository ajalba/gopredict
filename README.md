# GoPredict

GoPredict es un sitio web con el fin de dar a sus usuarios la oportunidad de realizar el ciclo de trabajo clásico de un modelo de predicción sin la necesidad de realizar instalaciones en su máquina. Este ciclo de trabajo generalmente se desarrolla de la siguiente forma:

- Se toma un conjunto de datos de entrenamiento, para entrenar al modelo
- Se divide este conjunto en train y test, el primero de ellos sirve para que el modelo aprenda y el segundo para ver su rendimiento, es decir, lo bien que ha aprendido a clasificar los datos
- Se toma un conjunto de datos que no estan clasificados, que se llama conjunto de test
- El modelo toma los datos y los clasifica, pudiendo descargar el resultado después

En el sitio web de GoPredict se podrá:

- Subir un conjunto de datos y elegir las características con las que trabajar
- Elegir un modelo para realizar predicciones
- Seleccionar los parámetros del modelo que se consideren mejores para el problema
- Entrenar el modelo viendo sus resultados
- Realizar predicciones con ese modelo y descargar los resultados

Esto puede servir como iniciación ligera al análisis de datos en un ámbito educativo y también puede servir a personas que conozcan el análisis de datos pero que por circunstancias no dispongan de una instalación completa en su máquina.

Proyecto actualmente en fase de planificación, versión 1.2.0

## Lógica de negocio

La lógica de negocio del proyecto se encuentra descrita [aquí](./docs/logica-negocio.md)

## Planificación

Las [milestones](https://github.com/ajalba/gopredict/milestones) definen los diferentes productos mínimos viables que atravesará el proyecto.

Mediante las [historias de usuario](./docs/historias-usuario.md) se puede ver el comportamiento de los usuarios cuando empleen la aplicación.

Los [user jouneys](./docs/user-journeys.md) representan a los distintos usuarios de la aplicación.

## Tareas

Es posible ver las tareas del proyesto [aquí](./docs/descripcion-tareas.md)

## Biblioteca de aserciones, marco de pruebas y gestor de tareas

El estudio y la elección de estas herramientas se encuentra [aquí](./docs/justificacion-herramientas.md)
