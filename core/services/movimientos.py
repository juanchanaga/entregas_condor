from django.db import transaction
from core.models import Producto

@transaction.atomic
def movimiento_inventario(producto_id, cantidad, tipo):
    """ tipo = 'entrada' o 'salida' """

    producto = Producto.objects.get(id=producto_id)

    if tipo == "entrada":
        producto.stock_disponible += cantidad

    elif tipo == "salida":
        if producto.stock_disponible < cantidad:
            raise ValueError("Inventario insuficiente")
        producto.stock_disponible -= cantidad

    else:
        raise ValueError("Tipo de movimiento no válido")

    producto.save()
    return producto
