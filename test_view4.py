import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "concesionaria.settings")
django.setup()

from django.test import RequestFactory
from inventario.views import index

factory = RequestFactory()
request = factory.get('/?ano=2024')
response = index(request)
html = response.content.decode('utf-8')
print("Total vehiculos en HTML:", html.count('class="car-card"'))

request2 = factory.get('/?ano=2019')
response2 = index(request2)
html2 = response2.content.decode('utf-8')
print("Total vehiculos 2019:", html2.count('class="car-card"'))

request3 = factory.get('/?ano=')
response3 = index(request3)
html3 = response3.content.decode('utf-8')
print("Total vehiculos vacio:", html3.count('class="car-card"'))

