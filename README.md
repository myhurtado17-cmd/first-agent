# Primer agente local

## Instalaciones

- Python.

- UV. Ingresar a la terminar, copiar y pegar la siguiente instrucción.

```bash
pip install uv
```

## Crear el proyecto.

1. Crear la carpeta del proyecto

2. Inicializar el proyecto con UV

```bash
uv init --name first-agent-gemini
```

3. Añadir todas las dependencias (uv crea el .env automáticamente).

```bash
uv add langchain langchain-google-genai langchain-community fastapi uvicorn python-dotenv
```

4. Instalar todas las dependencias del paso anterior.

```bash
uv sync
```

## API Key

1. Ir a AIStudio de Google.
2. Iniciar sesión con la cuenta de Google.
3. Crear la API key.
4. Copiar la API key.

## Archivos del proyecto

1. Crear un gitignore.
2. Crear .env

```javascript
GOOGLE_API_KEY = Pegar la API Key de la sección anterior
```

3. Crear el script app.py
