#usar la imagen oficial de uv
FROM ghcr.io/astral-sh/uv:latest AS builder

#copiar unicamente los archivos de dependencias
WORKDIR /app
COPY pyproject.toml uv.lock ./

#intalar uv sin pip
RUN uv install --frozen