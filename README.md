# Extractor de Texto de PDF

Este es un programa desarrollado en Python diseñado para extraer el contenido de texto de archivos PDF y convertirlo a un formato procesable (como Markdown o texto plano). Es ideal para procesar resúmenes, trabajos prácticos y documentos pesados.

## ⚙️ ¿Cómo funciona?

El script principal (`main.py`) toma los archivos PDF como entrada, los procesa utilizando librerías de extracción de texto y genera archivos de salida legibles y livianos. 

Para mantener el repositorio de GitHub optimizado y no superar los límites de tamaño (100 MB), los documentos PDF originales se guardan en una carpeta local llamada `defa/`, la cual está excluida del control de versiones mediante el archivo `.gitignore`.

## 🛠️ Requisitos

- Python 3.11 (definido en `.python-version`)

## 🚀 Instalación y Configuración del Entorno

Para ejecutar este proyecto en tu computadora, sigue estos pasos en tu terminal (por ejemplo, Git Bash en Windows):

**1. Crear el entorno virtual**
El entorno virtual (`.venv`) es una carpeta aislada donde se instalarán las librerías necesarias sin afectar al resto de tu computadora.
```bash
python -m venv .venv
```

**2. Activar el entorno virtual**
Debes ejecutar este comando cada vez que abras una nueva terminal para trabajar en el proyecto. Sabrás que está activo porque aparecerá `(.venv)` al principio de tu línea de comandos.
```bash
source .venv/Scripts/activate
```

**3. Instalar las dependencias (Librerías)**
Como el proyecto cuenta con un archivo `pyproject.toml` y `uv.lock`, significa que las librerías están declaradas allí. Para instalarlas, ejecuta:
```bash
pip install .
```
*(Nota alternativa: Si utilizas el gestor rápido `uv`, simplemente puedes ejecutar `uv sync` para crear el entorno e instalar todo automáticamente).*

**4. Ejecutar el programa**
Una vez instaladas las librerías, puedes correr el script principal con:
```bash
python main.py
```

---

### 💡 Explicación extra de los comandos:
* `python -m venv .venv`: Le dice a Python que cree un "entorno virtual" (una burbuja aislada) y que guarde todo en una carpeta llamada `.venv`. Al tenerla en el `.gitignore`, evitas que esta carpeta con miles de archivos de librerías se suba a GitHub.
* `source .venv/Scripts/activate`: Es el comando específico para Git Bash en Windows que "enciende" esa burbuja para empezar a trabajar dentro de ella.
* `pip install .`: En lugar de instalar librería por librería a mano, este comando lee el archivo de configuración de tu proyecto (`pyproject.toml`) e instala todas las dependencias necesarias de una sola vez.
