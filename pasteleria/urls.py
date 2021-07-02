from django.urls import path

from . import views
app_name = 'pasteleria'
urlpatterns = [
    path('', views.index, name='index'),
    path('frm_agregar_producto', views.frm_agregar_producto, name='frm_agregar_producto'),
    path('registrar_producto', views.registrar_producto, name='registrar_producto'),
    path('frm_buscar_producto', views.frm_buscar_producto, name='frm_buscar_producto'),
    path('buscar_producto', views.buscar_producto, name='buscar_producto'),
    path('eliminar/<id>', views.eliminar, name="eliminar"),
    path('modificar/<id>', views.modificar, name="modificar"),
    path('modificar_producto/<id>', views.modificar_producto, name="modificar_producto"),
]