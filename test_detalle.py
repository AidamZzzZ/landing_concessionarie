import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "concesionaria.settings")
django.setup()

from inventario.models import Vehiculo
from django.test import RequestFactory
from inventario.views import detalle

v = Vehiculo.objects.first()
if v:
    factory = RequestFactory()
    request = factory.get(f'/vehiculo/{v.id}/')
    response = detalle(request, v.id)
    print(response.status_code)
    print("Contiene Contactanos:", b'wa.me' in response.content)
else:
    print("No vehicles found")
