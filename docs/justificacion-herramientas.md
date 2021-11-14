# Justificación de las herramientas elegidas para el proyecto

## Biblioteca de aserciones

Se han considerado varias bibliotecas de aserciones como **Assertpy**, **Grappa** o **Verify**.
Se ha tomado la biblioteca **Asertpy** como biblioteca de asserciones del proyecto porque presenta un estilo bajo los estándares de python que es verbose y explicativo pero no demasiado, como Grappa, que es demasiado verbose y la escritura de asserciones es más larga y puede parecer redundante, los tests de asserpy son mucho más compactos. Por último, la biblioteca Verify se ha descartado debido a que la facilidad para leer e interpretar assertpy es mucho mayor y considero esto importante para una persona que no ha realizado muchos tests, como yo.

## Marco de pruebas

En cuanto a marcos de pruebas se han considerado [Pytest](https://docs.pytest.org/en/stable/), [Testify](https://github.com/Yelp/Testify) y [Nose2](https://docs.nose2.io/en/latest/) entre otros.

**Nose2**, sucesor de **Nose**, posee como base la biblioteca **Unittest** para la la realización de aserciones, algo que tiene en común con **Testify**. **Nose2** requiere un conocimiento previo dilatado sobre testing en Python, de hecho, la propia documentación anima a que si el usuario es nuevo en el empleo de tests, utilice **Pytest**. **Testify**, también basado en **Unittest**, goza de convenciones más similares a la propia de __python__ y con plugins que extienden su funcionalidad. Sin embargo la documentación no es tan extensa como la encontrada sobre **Pytest**.

Se ha seleccionado **Pytest** ya que permite tests compactos y sencillos de comprender, además de ser open source y ser de los marcos de pruebas más utilizados con una comunidad enorme, tiene varias extensiones como __pytest-cov__ para conocer el coverage de los test y __pytest-xdist__ para ejecutar test en paralelo por ejemplo.

Permite mejor integración con la biblioteca de aserciones, de hecho la propia documentación de la misma recomienda emplear **Pytest**.

Los test se definen como funciones, no como los frameworks basados en **Unittest** que requieren el uso de clases con herencia cuyos métodos representan los tests. Todo esto junto con el soporte de las __fixtures__ y el hecho de poder crear tests unitarios concisos y compactos han hecho que se seleccione esta opción.

## Gestor de Tareas

Como gestor de tareas para el proyecto se ha seleccionado **Invoke**, ya que es un gestor de tareas que sigue la sintaxis de python, a diferencia del **Makefile**, que tiene su propia sintaxis. Una característica a destacar es que al estar basado en python3, los errores de **Invoke** pueden verse como erroes de python, que indican donde esta el error exactamente. Los errores de **Makefile** pueden ser más difíciles de ver. Invoke es sencillo de integrar al igual que **GNU Make**, herramienta seleccionada anteriormente. Se estudio también la posibilidad de emplear **Poetry**, sin embargo es más difícil de integrar y es una herramienta compleja con gran cantidad de dependencias. Sin duda **Poetry** sería una muy buena opción para un gran proyecto, pero en este caso se considera que una herramienta como **Invoke** es más que suficiente, además de que es más ligera que **Poetry**, lo cual será bueno para ahorrar carga en el contenedor que se va a emplear más adelante.

Se ha instalado con **pip3**  y se ha creado el fichero de tareas, que en **Invoke** es el fichero [tasks.py](../tasks.py). En él se han definido las siguientes tareas:

- **invoke execute**: ejecuta la aplicación
- **invoke test**: ejecuta los tests unitarios
- **invoke clean**: realiza una limpieza de ficheros
- **invoke install**: realiza la instalación de las bibliotecas del archivo [requirements.txt](../requirements.txt)
