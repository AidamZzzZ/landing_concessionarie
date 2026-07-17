import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "concesionaria.settings")
django.setup()

from django.test import RequestFactory
from inventario.views import index

factory = RequestFactory()
request = factory.get('/?ano=2024')
response = index(request)
print(response.content.decode('utf-8').count('car-card'))
