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
FROM python:3.8-slim-buster as builder
ENV PATH="/home/gopredict/.local/bin:${PATH}"
RUN useradd -m gopredict \
	&& mkdir -p app/test \
	&& chown gopredict:gopredict -R /app/test
USER gopredict
WORKDIR /app/test
COPY tasks.py .
RUN pip install invoke && invoke install && rm tasks.py
ENTRYPOINT [ "invoke","test" ]