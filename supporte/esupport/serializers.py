from rest_framework import serializers
from .models import ProveedoresProducto,Proveedores,Oferta,CategoriaProducto,Perifericos, MarcaProducto, Producto, Cliente, TicketSoporte, Compra, ComentarioProducto, Carrito, ItemCarrito, Pedido, ItemPedido, MetodoPago, ValoracionResena, MensajeChat, Factura

class MarcaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaProducto
        fields = '__all__'

class PerifericosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perifericos
        fields = '__all__'

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'

class ProveedoresProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedoresProducto
        fields = '__all__'

class ProveedoresSerializer(serializers.ModelSerializer):
    productoproveedor = ProveedoresProductoSerializer()

    class Meta:
        model = Proveedores
        fields = '__all__'
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TicketSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketSoporte
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

class ComentarioProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioProducto
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class ItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrito
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__'

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'

class ValoracionResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValoracionResena
        fields = '__all__'

class MensajeChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensajeChat
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'
