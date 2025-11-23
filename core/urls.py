from django.urls import path
from core import views

urlpatterns = [
    path("", views.home_view, name="home"),

    # Procesos existentes
    path("registrar-pedido/", views.registrar_pedido_view, name="registrar_pedido"),
    path("confirmar-pago/", views.confirmar_pago_view, name="confirmar_pago"),
    path("movimiento-inventario/", views.movimiento_inventario_view, name="movimiento_inventario"),

    # Listados
    path("lista-pedidos/", views.lista_pedidos_view, name="lista_pedidos"),
    path("lista-productos/", views.lista_productos_view, name="lista_productos"),
    path("lista-clientes/", views.lista_clientes_view, name="lista_clientes"),
    path("lista-proveedores/", views.lista_proveedores_view, name="lista_proveedores"),
]
