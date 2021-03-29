# Technical test beTech

_Technical test for backend developer in Be TECH CAPITAL_

### Features 📋



```
* Endpoints para Registrar, Modificar, Listar y Eliminar usuarios y sus datos.
* Filtro de usuarios por nombre y sexo.
* Envío un mensaje de bienvenida por Whatsapp y Email.
* Tests Unitarios.
* Documentación de la API (Swagger y Redoc).
* Código en repositorio (Github)
* README con instrucciones para ejecutar la app.
* Despliegue del API en servidor.
```

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
Docker
Requirements.txt:
django==3.1.7
Markdown==3.3.4
django-filter==2.4.0
djangorestframework==3.12.4
psycopg2>=2.7,<3.0
django-ckeditor==5.9.0
Pillow==8.1.2
drf-yasg
requests~=2.25.1
```

### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Clonar el repositorio_

```
gh repo clone amtzran/technical-test-be-tech
```

_Crear el archivo .env a partir de .env-example_

```
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=1

POSTGRES_DB=test
POSTGRES_USER=admin_test
POSTGRES_PASSWORD=YOUR_PASSWORD
POSTGRES_HOST=db
POSTGRES_PORT=5432

EMAIL_HOST_USER=YOUR_ADDRESS_EMAIL
EMAIL_HOST_PASSWORD=YOUR_PASSWORD_EMAIL
```

_Construir el contenedor_

```
docker-compose build
```

_Levantar el contenedor_

```
docker-compose up -d
```

_Ejecutar las migraciones_

```
docker exec technical_test_be_tech_web_1 bash -c "python manage.py makemigrations" 
docker exec technical_test_be_tech_web_1 bash -c "python manage.py migrate" 
```

_Crear super usuario_

```
docker exec -ti technical_test_be_tech_web_1 bash
python manage.py createsuperuser
exit
```

## Documentación 📚

_Documentación del estándar openapi Api Rest._

* [Swagger](http://127.0.0.1:8000/)  ```http://127.0.0.1:8000/```
* [Redoc](http://127.0.0.1:8000/redoc/) ```http://127.0.0.1:8000/redoc/```

## Ejecutando las pruebas ⚙️

_Para ejecutar las pruebas unitarias:_

### Analice las pruebas REST Api 🔩

_Los unit tests que se encuentran en /users/tests.py comprueban la funcionalidad del CRUD users._

```
docker exec technical_test_be_tech_web_1 bash -c "python manage.py test"
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Python 3.9](https://www.python.org/) - El lenguaje de backend.
* [Django 3.1](https://www.djangoproject.com/) - El framework web usado.
* [Django REST Framework 3.12.4](https://www.django-rest-framework.org/) - Framework para construir API REST con python y Django.
* [Docker](https://www.docker.com/) - Automatización del despliegue y el entorno.
* [Docker compose](https://docs.docker.com/compose/) - Automatización del entorno y librerías.
* [PostgreSQL](https://www.postgresql.org/) - Sistema de base de datos relacional.
* [Pillow 8.1.2](https://pillow.readthedocs.io/en/stable/) - Uso de fotos para perfil de usuario.
* [Swagger & Redoc](https://drf-yasg.readthedocs.io/en/stable/) - Documentación API.
* [Requirements](https://blog.usejournal.com/why-and-how-to-make-a-requirements-txt-f329c685181e) - Manejador de dependencias.
* [Chat API](https://app.chat-api.com/testing) - Api para envío de mensajes por WhatsApp.
* [GitHub](https://github.com/) - Control de versiones.


## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️


* **Alberto Martínez** - *Trabajo Inicial* - [amtzran](https://github.com/amtzran)

## Licencia 📄

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* De antemano quiero agradecer 🍺  a **Sergio García** por creer en mi y darme oportunidad de continuar con el proceso de la vacante.



---
⌨️ con ❤️ por [Alberto Martínez](https://github.com/amtzran) 😊