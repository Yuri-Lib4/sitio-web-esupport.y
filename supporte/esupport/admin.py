from django.contrib import admin
from .models import ProveedoresProducto,Proveedores, Oferta,CategoriaProducto,Perifericos,MarcaProducto, Producto, Cliente, TicketSoporte, Compra, ComentarioProducto, Carrito, ItemCarrito, Pedido, ItemPedido, MetodoPago, ValoracionResena, MensajeChat, Factura

# Admin para el modelo MarcaProducto
class MarcaProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(MarcaProducto, MarcaProductoAdmin)

# Admin para el modelo Periféricos
class PerifericosAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion']

admin.site.register(Perifericos, PerifericosAdmin)

# Admin para el modelo CategoriaProducto
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
# Admin para el modelo Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['perifericos','categoria','nombre', 'marca', 'precio', 'stock']
    list_filter = ['marca']
    search_fields = ['nombre', 'descripcion']

admin.site.register(Producto, ProductoAdmin)

# Admin para el modelo Proveedores
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ['productoproveedor','marca']
    list_filter = ['marca']
    search_fields = ['productoproveedor', 'marca']

admin.site.register(Proveedores, ProveedoresAdmin)

# Admin para el modelo ProveedoresProducto
class ProveedoresProductoAdmin(admin.ModelAdmin):
    list_display = ['producto']
    list_filter = ['producto']
    search_fields = ['producto']

admin.site.register(ProveedoresProducto, ProveedoresProductoAdmin)



# Admin para el modelo Oferta
class OfertaAdmin(admin.ModelAdmin):
    list_display = ['nombreProducto','producto','descripcion','fecha_inicio', 'fecha_fin', 'descuento']
    list_filter = ['nombreProducto']
    search_fields = ['producto', 'descripcion']

admin.site.register(Oferta, OfertaAdmin)


# Admin para el modelo Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono', 'correo']

admin.site.register(Cliente, ClienteAdmin)

# Admin para el modelo TicketSoporte
class TicketSoporteAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'asunto', 'fecha_creacion', 'resuelto']
    list_filter = ['cliente', 'resuelto']
    search_fields = ['asunto', 'descripcion']

admin.site.register(TicketSoporte, TicketSoporteAdmin)

# Admin para el modelo Compra
class CompraAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'producto', 'cantidad', 'fecha_compra']
    list_filter = ['cliente', 'producto']
    search_fields = ['cliente__user__username', 'producto__nombre']

admin.site.register(Compra, CompraAdmin)

# Admin para el modelo ComentarioProducto
class ComentarioProductoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'producto', 'fecha_creacion']
    list_filter = ['cliente', 'producto']
    search_fields = ['cliente__user__username', 'producto__nombre']

admin.site.register(ComentarioProducto, ComentarioProductoAdmin)

# Admin para el modelo Carrito
class CarritoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'fecha_creacion']

admin.site.register(Carrito, CarritoAdmin)

# Admin para el modelo ItemCarrito
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ['carrito', 'producto', 'cantidad']

admin.site.register(ItemCarrito, ItemCarritoAdmin)

# Admin para el modelo Pedido
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'fecha_pedido']

admin.site.register(Pedido, PedidoAdmin)

# Admin para el modelo ItemPedido
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'producto', 'cantidad']

admin.site.register(ItemPedido, ItemPedidoAdmin)

# Admin para el modelo MetodoPago
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(MetodoPago, MetodoPagoAdmin)

# Admin para el modelo ValoracionResena
class ValoracionResenaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'producto', 'valoracion', 'fecha_creacion']
    list_filter = ['cliente', 'producto', 'valoracion']
    search_fields = ['cliente__user__username', 'producto__nombre']

admin.site.register(ValoracionResena, ValoracionResenaAdmin)

# Admin para el modelo MensajeChat
class MensajeChatAdmin(admin.ModelAdmin):
    list_display = ['emisor', 'receptor', 'contenido', 'fecha_envio']
    list_filter = ['emisor', 'receptor']
    search_fields = ['emisor__username', 'receptor__username']

admin.site.register(MensajeChat, MensajeChatAdmin)

# Admin para el modelo Factura
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'pedido', 'metodo_pago', 'fecha_emision', 'total']
    list_filter = ['cliente', 'metodo_pago']
    search_fields = ['cliente__user__username']

admin.site.register(Factura, FacturaAdmin)
