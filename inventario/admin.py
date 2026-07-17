from django.contrib import admin
from .models import Marca, Vehiculo, ImagenVehiculo

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class ImagenVehiculoInline(admin.TabularInline):
    model = ImagenVehiculo
    extra = 1

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'año', 'precio', 'estatus', 'destacado', 'fecha_creacion')
    list_filter = ('estatus', 'marca', 'año', 'destacado', 'transmision')
    search_fields = ('modelo', 'marca__nombre', 'id')
    list_editable = ('estatus', 'destacado', 'precio')
    inlines = [ImagenVehiculoInline]
