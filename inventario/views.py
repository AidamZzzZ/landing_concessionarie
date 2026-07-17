from django.shortcuts import render
from .models import Vehiculo, Marca

def index(request):
    # Base queryset for vehicles
    vehiculos = Vehiculo.objects.all()

    # Get filter parameters from the request
    marca_id = request.GET.get('marca')
    ano = request.GET.get('ano')

    # Apply filters if they exist
    if marca_id:
        vehiculos = vehiculos.filter(marca_id=marca_id)
    if ano:
        vehiculos = vehiculos.filter(año=ano)

    # Get all distinct brands and years for the filter dropdowns
    marcas = Marca.objects.all()
    # Get distinct years, flat list, order descending
    anos = Vehiculo.objects.values_list('año', flat=True).distinct().order_by('-año')

    context = {
        'vehiculos': vehiculos,
        'marcas': marcas,
        'anos': anos,
        'selected_marca': marca_id,
        'selected_ano': ano,
    }
    return render(request, 'inventario/index.html', context)
