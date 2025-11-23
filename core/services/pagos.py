from django.db import transaction
from core.models import Pedido, Transaccion_Pago

@transaction.atomic
def confirmar_pago(pedido_id, metodo, monto):
    pedido = Pedido.objects.get(id=pedido_id)

    if pedido.estado != "Pendiente":
        raise ValueError("El pedido no está pendiente de pago")

    transaccion = Transaccion_Pago.objects.create(
        pedido=pedido,
        metodo_pago=metodo,
        monto=monto,
        estado_pago="Aprobado"
    )

    pedido.estado = "Pagado"
    pedido.save()

    return transaccion
