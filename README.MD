# API PARA LA APLICACIÓN MARTITA_IA

Guía para la instalación, configuración y ejecución de la API del proyecto **MARTITA_IA**.

---

## 🚀 Instalación y Ejecución de la API

### 1. Crear el entorno virtual

```bash
python -m venv venv
```
### 2. Activar el entorno virtual

**En Windows:**
```bash
venv\Scripts\activate
```

**En Unix/macOS:**
```bash
source venv/bin/activate
```

### 3. Instalar los requerimientos

Instala las dependencias necesarias del proyecto:

```bash
pip install -r requirements.txt
```


### 4. Lanzar la aplicación

Ejecuta el servidor de desarrollo usando Uvicorn:

```bash
uvicorn app.main:app --reload
```

Esto ejecutará la API en modo desarrollo en `http://127.0.0.1:8000`.


Recomandacion , al realizar el docker file crea una imagen con linux y python 3.13.2
Agrega el path de la carpeta del proyecto en el docker file
