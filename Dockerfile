# Crea venv con la release de Debian correspondiente
# Instala python3-venv para el modulo v-env
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