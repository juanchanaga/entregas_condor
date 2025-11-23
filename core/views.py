from django.shortcuts import render
from core.models import Cliente, Producto, Pedido, Proveedor
from core.services.pedidos import registrar_pedido
from core.services.pagos import confirmar_pago
from core.services.inventario import actualizar_inventario
from core.services.movimientos import movimiento_inventario

def home_view(request):
    return render(request, "home.html")

def registrar_pedido_view(request):
    if request.method == "POST":
        cliente = Cliente.objects.first()
        producto_id = request.POST["producto"]
        cantidad = int(request.POST["cantidad"])

        pedido = registrar_pedido(cliente, producto_id, cantidad)

        return render(request, "registrar_pedido.html", {"pedido": pedido})

    productos = Producto.objects.all()
    return render(request, "registrar_pedido.html", {"productos": productos})


def confirmar_pago_view(request):
    if request.method == "POST":
        pedido_id = request.POST["pedido"]
        metodo = request.POST["metodo"]
        monto = float(request.POST["monto"])

        pago = confirmar_pago(pedido_id, metodo, monto)
        actualizar_inventario(pedido_id)

        return render(request, "confirmar_pago.html", {"pago": pago})

    return render(request, "confirmar_pago.html", {})


def movimiento_inventario_view(request):
    if request.method == "POST":
        producto_id = request.POST["producto"]
        cantidad = int(request.POST["cantidad"])
        tipo = request.POST["tipo"]

        resultado = movimiento_inventario(producto_id, cantidad, tipo)

        return render(request, "movimiento_inventario.html", {"producto": resultado})

    productos = Producto.objects.all()
    return render(request, "movimiento_inventario.html", {"productos": productos})


def lista_pedidos_view(request):
    pedidos = Pedido.objects.all().order_by('-fecha')
    return render(request, "lista_pedidos.html", {"pedidos": pedidos})


def lista_productos_view(request):
    productos = Producto.objects.all()
    return render(request, "lista_productos.html", {"productos": productos})


def lista_clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, "lista_clientes.html", {"clientes": clientes})


def lista_proveedores_view(request):
    proveedores = Proveedor.objects.all()
    return render(request, "lista_proveedores.html", {"proveedores": proveedores})
