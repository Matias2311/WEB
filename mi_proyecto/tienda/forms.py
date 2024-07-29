from django import forms
from .models import Cliente, Producto, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_usuario', 'contrasena', 'nombre_completo', 'email']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'producto', 'cantidad']

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
