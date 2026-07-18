import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "concesionaria.settings")
django.setup()

from django.template import Context, Template

template = Template("""
{% for ano in anos %}
<option value="{{ ano }}" {% if selected_ano == ano|stringformat:"s" %}selected{% endif %}>{{ ano }}</option>
{% endfor %}
""")
context = Context({
    'anos': [2024, 2020, 2019],
    'selected_ano': '2024'
})
print(template.render(context))
