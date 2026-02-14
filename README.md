# 🛒 Myth Store – Proyecto Django

Aplicación web desarrollada con **Python y Django** como proyecto del **Módulo 6**.  
Simula una tienda de productos **TCG** (Trading Card Games) como **Pokémon, Yu-Gi-Oh y Magic**.

Este proyecto está inspirado en una página TCG que administré hace algunos años, lo que permitió darle una estructura más realista y coherente.

---

## 🚀 Tecnologías utilizadas
- Python 3  
- Django  
- HTML5  
- CSS3

---

## ✅ Funcionalidades
- Página de inicio
- Listado de productos
- Detalle dinámico de productos (`/productos/<id>/`)
- Página "Nosotros"
- Formulario de contacto (modo demo con confirmación)
- Estilos personalizados (tema oscuro + morado)

---

## 🗂 Estructura del proyecto

myth_store/
├── config/ # Configuración del proyecto
├── store/ # App principal
│ ├── templates/ # Archivos HTML
│ ├── static/ # Archivos CSS
│ ├── views.py # Lógica de vistas
│ └── urls.py # Rutas
└── manage.py


---

## ⚙️ Instalación y ejecución

Clonar repositorio:

```bash
git clone https://github.com/OsvaldoGonzalezG/Proyecto-Myth-Store.git
cd Proyecto-Myth-Store
Crear y activar entorno virtual:

Windows

python -m venv venv
venv\Scripts\activate
Mac/Linux

python -m venv venv
source venv/bin/activate
Instalar dependencias:

pip install django
Ejecutar el servidor:

python manage.py runserver
Abrir en el navegador:

http://127.0.0.1:8000/
🧠 Conceptos aplicados
Configuración de rutas (URLs)

Vistas en Django

Templates con herencia

Uso de {% url %} para navegación dinámica

Archivos estáticos (CSS)

Manejo básico de formularios con método POST

Renderizado condicional con {% if %}

👤 Autor
Osvaldo Andrés González González
Proyecto académico – Desarrollo Web con Django
