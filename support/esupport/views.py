from rest_framework import generics
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import ProveedoresProducto,Proveedores,Oferta,CategoriaProducto,Perifericos,MarcaProducto, Producto, Cliente, TicketSoporte, Compra, ComentarioProducto, Carrito, ItemCarrito, Pedido, ItemPedido, MetodoPago, ValoracionResena, MensajeChat, Factura
from .serializers import ProveedoresProductoSerializer,ProveedoresSerializer,OfertaSerializer,CategoriaProductoSerializer,PerifericosSerializer, MarcaProductoSerializer, ProductoSerializer, ClienteSerializer, TicketSoporteSerializer, CompraSerializer, ComentarioProductoSerializer, CarritoSerializer, ItemCarritoSerializer, PedidoSerializer, ItemPedidoSerializer, MetodoPagoSerializer, ValoracionResenaSerializer, MensajeChatSerializer, FacturaSerializer


# esupport/views.py

from django.http import HttpResponse
from django.conf import settings
import os

def imagen_view(request, nombre_imagen):
    # Obtener la ruta absoluta de la imagen
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, nombre_imagen)
    try:
        # Abrir el archivo de la imagen y devolverlo como respuesta
        with open(ruta_imagen, 'rb') as file:
            return HttpResponse(file.read(), content_type="image/jpeg")
    except FileNotFoundError:
        return HttpResponse("Imagen no encontrada", status=404)


# Vistas para la API de MarcaProducto
class MarcaProductoListCreateView(generics.ListCreateAPIView):
    queryset = MarcaProducto.objects.all()
    serializer_class = MarcaProductoSerializer

class MarcaProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

class ProveedoresListCreateView(generics.ListCreateAPIView):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

class ProveedoresDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

class ProveedoresProductoListCreateView(generics.ListCreateAPIView):
    queryset = ProveedoresProducto.objects.all()
    serializer_class = ProveedoresProductoSerializer

class ProveedoresProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProveedoresProducto.objects.all()
    serializer_class = ProveedoresProductoSerializer

# Vistas para la API de Periféricos
class PerifericosListCreateView(generics.ListCreateAPIView):
    queryset = Perifericos.objects.all()
    serializer_class = PerifericosSerializer

class PerifericosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perifericos.objects.all()
    serializer_class = PerifericosSerializer

# def proveedores_list(request):
#     proveedores = Proveedores.objects.all()
#     data = [{'id': p.id, 'marca': p.marca, 'imagen': p.imagen.url} for p in proveedores]
#     return JsonResponse(data, safe=False)

# def proveedores_detalle(request, proveedor_id):
#     proveedor = Proveedores.objects.get(id=proveedor_id)
#     productos_relacionados = ProveedoresProducto.objects.filter(proveedor=proveedor)
#     data = {
#         'id': proveedor.id,
#         'marca': proveedor.marca,
#         'imagen': proveedor.imagen.url,
#         'productos_relacionados': [{'id': p.id, 'producto': p.producto} for p in productos_relacionados]
#     }
#     return JsonResponse(data)


# Vistas para la API de CategoriaProducto
class CategoriaProductoListCreateView(generics.ListCreateAPIView):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

class CategoriaProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

class ProductosPorCategoriaView(generics.ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        categoria_id = self.kwargs['categoria_id']
        categoria = get_object_or_404(CategoriaProducto, id=categoria_id)
        return Producto.objects.filter(categoria=categoria)
# Vistas para la API de Producto
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vistas para la API de Oferta
class OfertaListCreateView(generics.ListCreateAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer

class OfertaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer

# Vistas para la API de Cliente
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Vistas para la API de TicketSoporte
class TicketSoporteListCreateView(generics.ListCreateAPIView):
    queryset = TicketSoporte.objects.all()
    serializer_class = TicketSoporteSerializer

class TicketSoporteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketSoporte.objects.all()
    serializer_class = TicketSoporteSerializer

# Vistas para la API de Compra
class CompraListCreateView(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class CompraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

# Vistas para la API de ComentarioProducto
class ComentarioProductoListCreateView(generics.ListCreateAPIView):
    queryset = ComentarioProducto.objects.all()
    serializer_class = ComentarioProductoSerializer

class ComentarioProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComentarioProducto.objects.all()
    serializer_class = ComentarioProductoSerializer

# Vistas para la API de Carrito
class CarritoListCreateView(generics.ListCreateAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class CarritoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

# Vistas para la API de ItemCarrito
class ItemCarritoListCreateView(generics.ListCreateAPIView):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer

class ItemCarritoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer

# Vistas para la API de Pedido
class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# Vistas para la API de ItemPedido
class ItemPedidoListCreateView(generics.ListCreateAPIView):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

class ItemPedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

# Vistas para la API de MetodoPago
class MetodoPagoListCreateView(generics.ListCreateAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

class MetodoPagoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

# Vistas para la API de ValoracionResena
class ValoracionResenaListCreateView(generics.ListCreateAPIView):
    queryset = ValoracionResena.objects.all()
    serializer_class = ValoracionResenaSerializer

class ValoracionResenaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ValoracionResena.objects.all()
    serializer_class = ValoracionResenaSerializer

# Vistas para la API de MensajeChat
class MensajeChatListCreateView(generics.ListCreateAPIView):
    queryset = MensajeChat.objects.all()
    serializer_class = MensajeChatSerializer

class MensajeChatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MensajeChat.objects.all()
    serializer_class = MensajeChatSerializer

# Vistas para la API de Factura
class FacturaListCreateView(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class FacturaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

