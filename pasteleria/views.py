from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from pasteleria.models import Producto
from django.urls import reverse




def index(request):
    listado = Producto.objects.all()
    context = {'listado':listado}
    return render(request, 'pasteleria/index.html', context)

def frm_agregar_producto(request):
    return render(request, 'pasteleria/frm_agregar_producto.html')
def frm_registrar(request):
    return render(request, 'pasteleria/registrarse.html')

def iniciar_sesion(request):
    return render(request, 'pasteleria/iniciar sesion.html')

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
        return HttpResponseRedirect(reverse('pasteleria:index'))

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
        return HttpResponseRedirect(reverse('pasteleria:index'))   

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
    return HttpResponseRedirect(reverse('pasteleria:index'))

# def modificar(request,id):
#     id = Producto.objects.get(id=id)
#     listado = Producto.objects.all()
#     listado = {'listado':listado,'producto':id.producto, 'precio':id.precio, 'mensaje':id.mensaje,
#     'sabor':id.sabor, 'cantidad':id.cantidad}
#     return render(request, 'pasteleria/modificar.html', listado)

def modificar(request, id):
    producto = None
    lista = Producto.objects.get(id=id)
    producto = lista
    # if len(lista) > 0:
        
    # else:
    #     producto = None
    return render(request, 'pasteleria/modificar.html',{'producto':producto}) 
    # nombre_producto = lista.producto
    # precio_producto = lista.precio
    # mensaje_producto = lista.mensaje
    # sabor_prodcuto = lista.sabor
    # cantidad_producto = lista.cantidad

    
    
    
    