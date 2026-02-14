from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:id>/', views.producto_detalle, name='producto_detalle'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
]
