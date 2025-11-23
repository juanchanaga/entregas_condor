from django.db import transaction
from core.models import Pedido, Producto, Detalle_Pedido

@transaction.atomic
def actualizar_inventario(pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    detalles = Detalle_Pedido.objects.filter(pedido=pedido)

    for det in detalles:
        producto = det.producto

        if producto.stock_disponible < det.cantidad:
            raise ValueError("No hay stock suficiente")

        producto.stock_disponible -= det.cantidad
        producto.save()

    return True
