from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login
from django.conf.urls import url


from . import views
app_name = 'pasteleria'
urlpatterns = [
    path('', views.home, name='inicio'),
    path('productos', views.productos, name='productos'),
    path('frm_agregar_producto', views.frm_agregar_producto, name='frm_agregar_producto'),
    path('registrar_producto', views.registrar_producto, name='registrar_producto'),
    path('frm_buscar_producto', views.frm_buscar_producto, name='frm_buscar_producto'),
    path('buscar_producto', views.buscar_producto, name='buscar_producto'),
    path('eliminar/<id>', views.eliminar, name="eliminar"),
    path('modificar/<id>', views.modificar, name="modificar"),
    path('modificar_producto/<id>', views.modificar_producto, name="modificar_producto"),
    path('registro', views.frm_registrar, name='frm_registrar'),
    path('iniciar_sesion', views.Isesion, name='iniciar_sesion'),
    path('frm_registro', views.frm_registro, name='registro'),
    path('inicio_sesion', views.iniciar_sesion, name='inicio_sesion'),
    
]