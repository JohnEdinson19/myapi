# REST_API_CRUD

## Requisitos

- Python (versión X.X)
- pipenv

## Configuración del entorno virtual

1. Clona este repositorio:

   ```bash
   git clone https://github.com/JohnEdinson19/myapi.git

2. Navega al directorio del proyecto:
    cd myapi

3. Crea y activa el entorno virtual con pipenv
    pipenv install
    pipenv shell

## Configuración de la base de datos
1. Realiza las migraciones:
    pipenv run python manage.py migrate
2. Crea un superusuario
    pipenv run python manage.py createsuperuser

## Ejecutar la aplicación
1. Inicia el servidor de desarrollo:
    pipenv run python manage.py runserver
2. Abre tu navegador y visita http://localhost:8000/