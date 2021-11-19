# Documentación del Dockerfile

## Elección de la imagen

La aplicación hace uso de un conjunto de librerías especificadas en el archivo __requirements.txt__, por tanto se ha decidido emplear una imagen de docker que haga uso de un entorno virtual. Si se emplea una construcción multistage es posible tener una imagen pesada donde se construya el entorno virtual y se hagan todas las instalaciones necesarias, y a partir de ella construir una imagen con solo el entorno virtual.

Dentro de todas las imágenes posibles, se ha decidido emplear una imagen distroless, que contenga simplemente las dependencias de nuestra aplicación, así se restringe lo que hay en el contenedor a únicamente lo necesario. Esto es una práctica empleada por Google y otras grandes empresas tecnológicas con años de experiencia en contenedores.

Se ha decidido emplear una imagen de Debian como base, ya que la imagen distroless de python3 esta basada en Debian. Sobre esta base se ha instalado python3-venv para hacer uso de dicho módulo, se ha creado un paso de **build-venv** para ejecutar crear el entorno virtual solo cuando cambie el archivo __requirements.txt__. Finalmente se crea la imagen final partiendo de una imagen distroless y copiando el virtualenv.

Dado que el objetivo es poder ejecutar nuestro contenedor como un entorno de test, indicando como parámetro en la creación del mismo el directorio local y el directorio donde se debe montar en nuestro contenedor el directorio que contiene nuestro proyecto, no es necesario copiar nada en la imagen. Un ejemplo de esto sería el mostrado en los apuntes: **docker run -t -v `pwd`:/app/test nick-estudiante/nombre-del-repo**.

Se han considerado otras imágenes como **python3.9** como base y **python3.9-slim** para la imagen final, pero su tamaño es unos 100MB mayor y se descarta para favorecer las imágenes distroless.

## Dockerfile

El fichero __Dockerfile__ se ha construido intentando conseguir el menor número de capas, creando una orden run que enlaza comandos y haciendo una build multi stage donde cada stage toma únicamente lo necesario del anterior. La base del fichero proviene del repositorio [distroless](https://github.com/GoogleContainerTools/distroless/tree/main/examples/python3-requirements) de GoogleContarinerTools.

Finalmente el fichero __Dockerfile__ se ha construido como se puede ver a continuación.

```dockerfile
# Crea venv con la release de Debian correspondiente
# Instala python3-venv para el modulo venv
# En el virtualenv, actualiza pip setuputils para construir nuevos paquetes
FROM debian:11-slim AS build
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel
# Hacemos el virtualenv como un paso separado 
# para reejecutar este paso solo cuando cambie requirements.txt
FROM build AS build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

# Copiar el virtualenv a la imagen distroless
FROM gcr.io/distroless/python3-debian11
COPY --from=build-venv /venv /venv
WORKDIR /app/test
ENTRYPOINT ["/venv/bin/pytest"]
```
