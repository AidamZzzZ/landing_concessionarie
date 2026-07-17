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
import re
for match in re.finditer(r'<option[^>]*>.*?2024.*?</option>', html, re.DOTALL):
    print(match.group(0))
