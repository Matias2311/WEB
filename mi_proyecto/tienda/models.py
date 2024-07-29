from django.db import models

class Cliente(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    nombre_completo = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nombre_usuario

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.cliente} - {self.producto}"
