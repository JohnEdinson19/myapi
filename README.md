# REST_API_CRUD

## Requisitos

- Python (versión 3.8)
- pipenv

## Configuración del entorno virtual

1. Clona este repositorio:

   ```bash
   git clone https://github.com/JohnEdinson19/myapi.git

2. Navega al directorio del proyecto:
    ```bash
    cd myapi

3. Crea y activa el entorno virtual con pipenv
    ```bash
    pip install pipenv
    pipenv shell
    
3. Instala las librerias
    ```bash
    pipenv install -r requirements.txt

## Configuración de la base de datos
1. Realiza las migraciones:
    ```bash
    pipenv run python manage.py makemigrations
    pipenv run python manage.py migrate

2. Crea un superusuario
    ```bash
    pipenv run python manage.py createsuperuser

## Ejecutar la aplicación
1. Inicia el servidor de desarrollo:
    ```bash
    pipenv run python manage.py runserver
2. Abre tu navegador y visita http://localhost:8000/
