from django.shortcuts import render, redirect
from .models import Cliente, Producto, Pedido
from .forms import ClienteForm, ProductoForm, PedidoForm, BuscarForm

def index(request):
    return render(request, 'tienda/index.html')

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'tienda/registrar_cliente.html', {'form': form})

def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'tienda/registrar_producto.html', {'form': form})

def registrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PedidoForm()
    return render(request, 'tienda/registrar_pedido.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Producto.objects.filter(nombre__icontains=query)
            return render(request, 'tienda/resultados.html', {'resultados': resultados})
    else:
        form = BuscarForm()
    return render(request, 'tienda/buscar.html', {'form': form})
