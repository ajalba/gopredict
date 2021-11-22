from invoke import task, run

# Tarea de ejecución de la aplicación
@task
def execute(c):
    run('streamlit run ./gopredict/__main__.py')

#Tarea ejecución de los tests unitarios con pytest
@task
def test(c):
    run("pytest")

#Tarea de limpieza de ficheros de python
@task
def clean(c):
    print("Limpiando archivos de python")
    run("rm -rf .pytest_cache")
    print("Archivos eliminados")

#Tarea de instalacion de dependencias
@task
def install(c):
    print("Realizando instalación de bibliotecas")
    run("pip install pandas==1.3.4\
        sklearn==0.0\
        numpy==1.21.3\
        keras==2.6.0\
        plotly==5.3.1\
        streamlit==1.1.0\
        assertpy==1.1\
        pytest==6.2.5\
        pytest-mock==3.6.1")
    print("Bibliotecas instaladas")