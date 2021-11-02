# Justificación de las herramientas elegidas para el proyecto

## Biblioteca de aserciones

Se han considerado varias bibliotecas de aserciones como **Assertpy**, **Grappa** o **Verify**.
Se ha tomado la biblioteca **Asertpy** como biblioteca de asserciones del proyecto porque presenta un estilo bajo los estándares de python que es verbose y explicativo pero no demasiado, como Grappa, que es demasiado verbose y la escritura de asserciones es más larga y puede parecer redundante, los tests de asserpy son mucho más compactos. Por último, la biblioteca Verify se ha descartado debido a que la facilidad para leer e interpretar assertpy es mucho mayor y considero esto importante para una persona que no ha realizado muchos tests, como yo.

## Marco de pruebas

En cuanto a marcos de pruebas se han considerado **Pytest**, **Unittest** y **Nose2** entre otros.

Se ha descartado **Unittest** ya que la sintaxis a veces no presenta suficiente claridad y parece repetir código que presenta poca variación. Al venir de Junit, framework con el que no estoy habituado, también presenta una curva de dificultad más alta y mantiene CamelCase, que no es un defecto, pero el estándar de python es el snake_case. Ya que **Nose2** es en esencia una extensión de **Unittest** con plugins presenta los mismos inconvenientes que éste además de que no se ha encontrado que exista mucha documentación, por lo que se ha descartado.

Se ha seleccionado **Pytest** ya que permite tests compactos y sencillos de comprender, además de ser open source y ser de los marcos de pruebas más utilizados con una comunidad enorme, tiene varias extensiones como __pytest-cov__ para conocer el coverage de los test y __pytest-xdist__ para ejecutar test en paralelo por ejemplo. Todo esto junto con el soporte de las __fixtures__ y el hecho de poder crear tests unitarios concisos y compactos han hecho que se seleccione esta opción.

## Gestor de Tareas

Muchos proyectos de python no incluyen un gestor de tareas ya que python no es un lenguaje compilado y al no ser común que aparezca, es excluido. Se ha seleccionado como gestor de tareas GNU make con 4 objetivos intuitivos como son run, test, clean e install. Es una herramienta sencilla de usar y que generalmente todo sistema linux ya tiene instalado. De esta forma el proyecto es reproducible y las tareas se realizan con comandos que normalmente son conocidos por la comunidad.
