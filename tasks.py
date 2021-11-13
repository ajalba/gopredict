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
    run("rm -rf .pytest_cache .coverage coverage.xml")
    print("Archivos eliminados")

#Tarea de instalacion de dependencias
@task
def install(c):
    print("Realizando instalación de bibliotecas")
    run("pip install -r requirements.txt")
    print("Bibliotecas instaladas")