from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/<uuid:vehiculo_id>/', views.detalle, name='detalle'),
]
