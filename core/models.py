from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    contacto = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=100)
    stock_disponible = models.IntegerField(default=0)
    stock_en_transito = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="Pendiente")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nombre}"


class Detalle_Pedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)


class Transaccion_Pago(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.RESTRICT)
    metodo_pago = models.CharField(max_length=50)
    estado_pago = models.CharField(max_length=20, default="Pendiente")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)


class Orden_Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.RESTRICT)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="Creada")


class Detalle_Orden_Compra(models.Model):
    orden_compra = models.ForeignKey(Orden_Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

