from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar_producto/', views.registrar_producto, name='registrar_producto'),
    path('registrar_pedido/', views.registrar_pedido, name='registrar_pedido'),
    path('buscar/', views.buscar, name='buscar'),
]
