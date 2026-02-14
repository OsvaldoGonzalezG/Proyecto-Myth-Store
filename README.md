Myth Store – Proyecto Django

Aplicación web desarrollada con Python y Django como proyecto del Módulo 6.
Simula una tienda de productos TCG (Trading Card Games) como Pokémon, Yu-Gi-Oh y Magic.

Este proyecto está inspirado en una página TCG que administré hace algunos años, lo que permitió darle una estructura más realista y coherente.

- Tecnologías utilizadas

Python 3

Django

HTML5

CSS3

- Funcionalidades

✔ Página de inicio
✔ Listado de productos
✔ Detalle dinámico de productos (/productos/<id>/)
✔ Página "Nosotros"
✔ Formulario de contacto (modo demo con mensaje de confirmación)
✔ Diseño moderno con estilos personalizados

- Estructura del Proyecto
myth_store/
│
├── config/                # Configuración principal del proyecto
├── store/                 # Aplicación principal
│   ├── templates/         # Archivos HTML
│   ├── static/            # Archivos CSS
│   ├── views.py           # Lógica de vistas
│   └── urls.py            # Rutas de la aplicación
│
├── manage.py
└── .gitignore

- Instalación y ejecución

1️⃣ Clonar el repositorio:

git clone https://github.com/TU-USUARIO/myth-store-django.git
cd myth-store-django


2️⃣ Crear entorno virtual (opcional pero recomendado):

python -m venv venv


3️⃣ Activar entorno virtual:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


4️⃣ Instalar Django:

pip install django


5️⃣ Ejecutar servidor:

python manage.py runserver


Abrir en el navegador:

http://127.0.0.1:8000/

- Conceptos aplicados

Configuración de rutas (URLs)

Vistas en Django

Templates con herencia

Uso de {% url %} para navegación dinámica

Archivos estáticos (CSS)

Manejo básico de formularios con método POST

Renderizado condicional con {% if %}

🎯 Objetivo del Proyecto

Aplicar los fundamentos de Django comprendiendo el flujo:

URL → Vista → Template → Respuesta al navegador

- Desarrollador

Osvaldo Andrés González González
Proyecto académico – Desarrollo Web con Django
