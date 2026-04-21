from django.urls import path

from .api.views import CompraAPIView, LibroListAPIView
from .views import CompraRapidaView, CompraView, compra_rapida_fbv

urlpatterns = [
    # Vistas HTML
    path('compra/<int:libro_id>/', CompraView.as_view(), name='finalizar_compra'),
    path('compra-rapida-fbv/<int:libro_id>/', compra_rapida_fbv, name='compra_rapida_fbv'),
    path('compra-rapida/<int:libro_id>/', CompraRapidaView.as_view(), name='compra_rapida'),

    # API REST
    path('api/v1/libros/', LibroListAPIView.as_view(), name='api_libros'),
    path('api/v1/comprar/', CompraAPIView.as_view(), name='api_comprar'),
]