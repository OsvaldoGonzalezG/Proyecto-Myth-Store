from django.shortcuts import render

def home(request):
    return render(request, 'store/home.html')

from django.shortcuts import render

PRODUCTOS = [
    {"id": 1, "nombre": "Booster Pokémon", "precio": 4500, "descripcion": "Sobres originales para ampliar tu colección Pokémon."},
    {"id": 2, "nombre": "Booster Yu-Gi-Oh", "precio": 4000, "descripcion": "Cartas para mejorar tu deck y estrategias Yu-Gi-Oh."},
    {"id": 3, "nombre": "Deck Magic", "precio": 12000, "descripcion": "Deck listo para jugar. Ideal para empezar o mejorar tu estilo."},
]

def home(request):
    return render(request, 'store/home.html')

def productos(request):
    return render(request, 'store/productos.html', {"productos": PRODUCTOS})

def producto_detalle(request, id):
    producto = next((p for p in PRODUCTOS if p["id"] == id), None)

    if producto is None:
        return render(request, 'store/404.html', status=404)

    return render(request, 'store/detalle.html', {"producto": producto})

def nosotros(request):
    return render(request, 'store/nosotros.html')

def contacto(request):
    enviado = False
    if request.method == "POST":
        enviado = True
    return render(request, 'store/contacto.html', {"enviado": enviado})


def nosotros(request):
    return render(request, 'store/nosotros.html')

def contacto(request):
    enviado = False

    if request.method == "POST":
        enviado = True

    return render(request, 'store/contacto.html', {"enviado": enviado})



