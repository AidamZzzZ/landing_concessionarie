import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "concesionaria.settings")
django.setup()

from inventario.models import Vehiculo, Marca

m = Marca.objects.first()
v = Vehiculo.objects.create(marca=m, modelo="Test", año=2023, precio=10000, kilometraje=0, transmision="automática", combustible="gasolina", color="rojo")

from django.test import Client
c = Client()
response = c.get('/?ano=2023')
print(response.content.decode('utf-8').count('car-card'))
