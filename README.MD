````markdown
# Instalación y Ejecución de la API

## 1. Crear el entorno virtual

```bash
python -m venv venv
````

## 2. Activar el entorno virtual

### En Windows:

```bash
venv\Scripts\activate
```

### En Unix/macOS:

```bash
source venv/bin/activate
```

## 3. Instalar los requerimientos

```bash
pip install -r requirements.txt
```

## 4. Lanzar la aplicación

```bash
uvicorn app.main:app --reload
```

```

Recomandacion , al realizar el docker file crea una imagen con linux y python 3.13.2
Agrega el path de la carpeta del proyecto en el docker file
