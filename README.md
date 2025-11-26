## Tecnologías Utilizadas

* **Backend:** Python 3.x, Django 5.x
* **Base de Datos:** PostgreSQL (en producción) / SQLite (en desarrollo)
* **Estilo:** Bootstrap
* **Generación de PDF:** ReportLab
* **Web Scraping:** `requests` y `BeautifulSoup4`
* **Deploy:** Render

---



## Instrucciones de Instalación Local

Para correr este proyecto en tu entorno local:

 **Crear y activar el entorno virtual:**
    ```bash
    python -m venv .venv
    # En Windows PowerShell:
    .\.venv\Scripts\activate
    ```
  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
 **Configurar Correo (Local):** En `proyecto_parcial/settings.py`, usa el backend de consola para ver los correos en la terminal:
    ```python
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
    ```
5.  **Migrar la base de datos y crear superusuario:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```
6.  **Iniciar el servidor:**
    ```bash
    python manage.py runserver
    ```
   `http://127.0.0.1:8000/`