from django.shortcuts import render, get_object_or_404
from .models import Vehiculo, Marca

def index(request):
    # Base queryset for vehicles
    vehiculos = Vehiculo.objects.all()

    # Get filter parameters from the request
    marca_id = request.GET.get('marca')
    ano = request.GET.get('ano')
    
    selected_marca = None
    selected_ano = None

    # Apply filters if they exist
    if marca_id:
        try:
            selected_marca = int(marca_id)
            vehiculos = vehiculos.filter(marca_id=selected_marca)
        except ValueError:
            pass
            
    if ano:
        try:
            selected_ano = int(ano)
            vehiculos = vehiculos.filter(año=selected_ano)
        except ValueError:
            pass

    # Get all distinct brands and years for the filter dropdowns
    marcas = Marca.objects.all()
    # Get distinct years, flat list, order descending
    anos = Vehiculo.objects.values_list('año', flat=True).distinct().order_by('-año')

    context = {
        'vehiculos': vehiculos,
        'marcas': marcas,
        'anos': anos,
        'selected_marca': selected_marca,
        'selected_ano': selected_ano,
    }
    return render(request, 'inventario/index.html', context)

def detalle(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    imagenes = vehiculo.imagenes.all()
    
    context = {
        'vehiculo': vehiculo,
        'imagenes': imagenes,
    }
    return render(request, 'inventario/detalle.html', context)
