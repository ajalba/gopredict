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

Muchos proyectos de python no incluyen un gestor de tareas ya que python no es un lenguaje compilado y al no ser común que aparezca, es excluido. Se ha seleccionado como gestor de tareas GNU make con 4 objetivos intuitivos como son run, test, clean e install. Es una herramienta sencilla de usar y que generalmente todo sistema linux ya tiene instalado. De esta forma el proyecto es reproducible y las tareas se realizan con comandos que normalmente son conocidos por la comunidad.
