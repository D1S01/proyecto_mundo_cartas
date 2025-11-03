from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.

# <---------------vistas de producto------------>
def ProductoListView(request):
    return render(request, 'tienda/producto/producto_list.html', {'productos':Producto.objects.all()})

def ProductoCreateView(request):
    if request.method=="POST":
        form=ProductoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('producto-list')
    else:
        form=ProductoForm()
    return render(request, 'tienda/producto/producto_form.html', {'form':form, 'action':'Crear'})

def ProductoDeleteView(request, id):
    producto=get_object_or_404(Producto, pk=id)
    if request.method=="POST":
        producto.delete()
        return redirect('producto-list')
    return render(request, 'tienda/producto/producto_delete.html')

def ProductoUpdateView(request, id):
    producto=get_object_or_404(Producto, pk=id)
    if request.method=="POST":
        form=ProductoForm(request.POST or None, request.FILES or None, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto-list')
    else:
        form=ProductoForm(instance=producto)
    return render(request, 'tienda/producto/producto_form.html', {'form':form, 'action':'Modificar'})

# <---------------vistas de categoria------------>

def CategoriaListView(request):
    return render(request, 'tienda/categoria/categoria_list.html', {'categorias':Categoria.objects.all()})

def CategoriaCreateView(request):
    if request.method=="POST":
        form=CategoriaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('categoria-list')
    else:
        form=CategoriaForm()
    return render(request, 'tienda/categoria/categoria_form.html', {'form':form, 'action':'Crear'})

def CategoriaDeleteView(request, id):
    categoria=get_object_or_404(Categoria, pk=id)
    if request.method=="POST":
        categoria.delete()
        return redirect('categoria-list')
    return render(request, 'tienda/categoria/categoria_delete.html')
