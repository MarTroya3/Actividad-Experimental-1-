"""
    Manejo de urls para la aplicación
"""
from django.urls import path
# se importa las vistas de la aplicación

from inventario import views


urlpatterns = [
        path('', views.stock, name='stock'),
 ]