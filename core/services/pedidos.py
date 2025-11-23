from django.db import transaction
from core.models import Pedido, Detalle_Pedido, Producto

@transaction.atomic
def registrar_pedido(cliente, producto_id, cantidad):
    producto = Producto.objects.get(id=producto_id)

    if producto.stock_disponible < cantidad:
        raise ValueError("No hay suficiente inventario disponible")

    precio = 10000  # valor ejemplo

    pedido = Pedido.objects.create(
        cliente=cliente,
        estado="Pendiente",
        total=precio * cantidad
    )

    Detalle_Pedido.objects.create(
        pedido=pedido,
        producto=producto,
        cantidad=cantidad,
        precio_unitario=precio
    )

    return pedido
