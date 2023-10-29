from django.urls import path
from . import views
from .views import (
    CategoriaProductoListCreateView,
    ProveedoresListCreateView,
    ProveedoresDetailView,
    imagen_view,
    CategoriaProductoDetailView,
    PerifericosListCreateView,
    PerifericosDetailView,
    MarcaProductoListCreateView,
    MarcaProductoDetailView,
    ProductoListCreateView,
    ProductoDetailView,
    OfertaListCreateView,
    OfertaDetailView,
    ClienteListCreateView,
    ClienteDetailView,
    TicketSoporteListCreateView,
    TicketSoporteDetailView,
    CompraListCreateView,
    CompraDetailView,
    ComentarioProductoListCreateView,
    ComentarioProductoDetailView,
    CarritoListCreateView,
    CarritoDetailView,
    ItemCarritoListCreateView,
    ItemCarritoDetailView,
    PedidoListCreateView,
    PedidoDetailView,
    ItemPedidoListCreateView,
    ItemPedidoDetailView,
    MetodoPagoListCreateView,
    MetodoPagoDetailView,
    ValoracionResenaListCreateView,
    ValoracionResenaDetailView,
    MensajeChatListCreateView,
    MensajeChatDetailView,
    FacturaListCreateView,
    FacturaDetailView,
    ProveedoresProductoListCreateView,
    ProveedoresProductoDetailView
)

urlpatterns = [
    # URLs para MarcaProducto
    path('marca-producto/', MarcaProductoListCreateView.as_view(), name='marca-producto-list-create'),
    path('marca-producto/<int:pk>/', MarcaProductoDetailView.as_view(), name='marca-producto-detail'),
    path('marca-producto/<str:nombre_imagen>/', imagen_view, name='imagen-view'),

    # URLs para Periféricos
    path('perifericos/', PerifericosListCreateView.as_view(), name='perifericos-list-create'),
    path('perifericos/<int:pk>/', PerifericosDetailView.as_view(), name='perifericos-detail'),
    path('perifericos/<str:nombre_imagen>/', imagen_view, name='imagen-view'),

    # URLs para Proveedores
    path('proveedores/', ProveedoresListCreateView.as_view(), name='proveedores-list-create'),
    path('proveedores/<int:pk>/', ProveedoresDetailView.as_view(), name='proveedores-detail'),
    path('proveedores/<str:nombre_imagen>/', imagen_view, name='imagen-view'),

    # URLs para ProveedoresProductos
    path('proveedores-producto/', ProveedoresProductoListCreateView.as_view(), name='proveedores-producto-list-create'),
    path('proveedores-producto/<int:pk>/', ProveedoresProductoDetailView.as_view(), name='proveedores-producto-detail'),

    # URLs para CategoriaProducto
    path('categoria-producto/', CategoriaProductoListCreateView.as_view(), name='categoria-producto-list-create'),
    path('categorias/<int:categoria_id>/productos/', views.ProductosPorCategoriaView.as_view(), name='productos-por-categoria'),
    path('categoria-producto/<int:pk>/', CategoriaProductoDetailView.as_view(), name='categoria-producto-detail'),

    # URLs para Producto
    path('producto/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),

    # URLs para Oferta
    path('oferta/', OfertaListCreateView.as_view(), name='Oferta-list-create'),
    path('oferta/<int:pk>/', OfertaDetailView.as_view(), name='Oferta-detail'),

    # URLs para Cliente
    path('cliente/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),

    # URLs para TicketSoporte
    path('ticket-soporte/', TicketSoporteListCreateView.as_view(), name='ticket-soporte-list-create'),
    path('ticket-soporte/<int:pk>/', TicketSoporteDetailView.as_view(), name='ticket-soporte-detail'),

    # URLs para Compra
    path('compra/', CompraListCreateView.as_view(), name='compra-list-create'),
    path('compra/<int:pk>/', CompraDetailView.as_view(), name='compra-detail'),

    # URLs para ComentarioProducto
    path('comentario-producto/', ComentarioProductoListCreateView.as_view(), name='comentario-producto-list-create'),
    path('comentario-producto/<int:pk>/', ComentarioProductoDetailView.as_view(), name='comentario-producto-detail'),

    # URLs para Carrito
    path('carrito/', CarritoListCreateView.as_view(), name='carrito-list-create'),
    path('carrito/<int:pk>/', CarritoDetailView.as_view(), name='carrito-detail'),

    # URLs para ItemCarrito
    path('item-carrito/', ItemCarritoListCreateView.as_view(), name='item-carrito-list-create'),
    path('item-carrito/<int:pk>/', ItemCarritoDetailView.as_view(), name='item-carrito-detail'),

    # URLs para Pedido
    path('pedido/', PedidoListCreateView.as_view(), name='pedido-list-create'),
    path('pedido/<int:pk>/', PedidoDetailView.as_view(), name='pedido-detail'),

    # URLs para ItemPedido
    path('item-pedido/', ItemPedidoListCreateView.as_view(), name='item-pedido-list-create'),
    path('item-pedido/<int:pk>/', ItemPedidoDetailView.as_view(), name='item-pedido-detail'),

    # URLs para MetodoPago
    path('metodo-pago/', MetodoPagoListCreateView.as_view(), name='metodo-pago-list-create'),
    path('metodo-pago/<int:pk>/', MetodoPagoDetailView.as_view(), name='metodo-pago-detail'),

    # URLs para ValoracionResena
    path('valoracion-resena/', ValoracionResenaListCreateView.as_view(), name='valoracion-resena-list-create'),
    path('valoracion-resena/<int:pk>/', ValoracionResenaDetailView.as_view(), name='valoracion-resena-detail'),

    # URLs para MensajeChat
    path('mensaje-chat/', MensajeChatListCreateView.as_view(), name='mensaje-chat-list-create'),
    path('mensaje-chat/<int:pk>/', MensajeChatDetailView.as_view(), name='mensaje-chat-detail'),

    # URLs para Factura
    path('factura/', FacturaListCreateView.as_view(), name='factura-list-create'),
    path('factura/<int:pk>/', FacturaDetailView.as_view(), name='factura-detail'),
]
