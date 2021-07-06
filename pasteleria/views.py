

import pasteleria
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from pasteleria.models import Cliente, Producto
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages




def productos(request):
    listado = Producto.objects.all()
    context = {'listado':listado}
    return render(request, 'pasteleria/index.html', context)


def frm_agregar_producto(request):
    return render(request, 'pasteleria/frm_agregar_producto.html')
def frm_registrar(request):
    return render(request, 'pasteleria/registrarse.html')



def registrar_producto(request):
    producto = request.POST['producto'].strip()
    precio = request.POST['precio'].strip()
    descripcion = request.POST['mensaje']
    sabor = request.POST['sabor'].strip()
    cantidad = request.POST['cantidad'].strip()
    if producto == "" or precio == "" or sabor == "" or cantidad == "":
        return HttpResponse("Debe ingresar los campos solicitados")
    else:
        guardar = Producto(producto=producto, precio=precio, descripcion=descripcion, sabor=sabor, cantidad=cantidad)
        guardar.save()
        return HttpResponseRedirect(reverse('pasteleria:productos'))

def modificar_producto(request, id):
    uProducto = Producto.objects.get(id=id)
    uProducto.producto = request.POST['producto']
    uProducto.precio = request.POST['precio']
    uProducto.mensaje = request.POST['mensaje']
    uProducto.sabor = request.POST['sabor']
    uProducto.cantidad = request.POST['cantidad']
    if uProducto.producto == "" or uProducto.precio == "" or uProducto.sabor == "" or uProducto.cantidad == "":
        return HttpResponse("Debe ingresar los campos solicitados")
    else:
        uProducto.save()
        return HttpResponseRedirect(reverse('pasteleria:productos'))   

def frm_buscar_producto(request):
    return render(request, 'pasteleria/frm_buscar_producto.html')

def buscar_producto(request):
    producto = request.POST['producto']
    listado = Producto.objects.filter(producto__startswith=producto)
    context = {'listado': listado}
    return render(request, 'pasteleria/busqueda.html', context)

  
def eliminar(request, id):
    id = Producto.objects.get(id=id)
    id.delete()
    return HttpResponseRedirect(reverse('pasteleria:productos'))


def modificar(request, id):
    producto = None
    lista = Producto.objects.get(id=id)
    producto = lista

    return render(request, 'pasteleria/modificar.html',{'producto':producto}) 

def home(request):
    return render(request, 'pasteleria/home.html')

def Isesion(request):
    return render(request, 'pasteleria/iniciar_sesion.html')

def frm_registro(request):
    return render(request, 'pasteleria/registrarse.html')




def iniciar_sesion(request):
    usuario = request.POST['rut']
    clave = request.POST['contraseña']
    user = authenticate(request, username=usuario, password=clave)
    
    if user is not None:
        login(request, user)
        return render(request, 'pasteleria/home.html')
    else:
        return render(request, 'pasteleria/iniciar_sesion.html')
    
    
    