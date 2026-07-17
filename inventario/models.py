import uuid
from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['nombre']

class Vehiculo(models.Model):
    ESTATUS_CHOICES = [
        ('disponible', 'Disponible'),
        ('no disponible', 'No Disponible'),
    ]

    TRANSMISION_CHOICES = [
        ('automática', 'Automática'),
        ('sincrónica', 'Sincrónica'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='vehiculos')
    modelo = models.CharField(max_length=150)
    año = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=2, help_text="Precio en USD")
    kilometraje = models.PositiveIntegerField()
    transmision = models.CharField(max_length=20, choices=TRANSMISION_CHOICES)
    combustible = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    estatus = models.CharField(max_length=20, choices=ESTATUS_CHOICES, default='disponible')
    destacado = models.BooleanField(default=False)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.marca.nombre} {self.modelo} ({self.año})"

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ['-destacado', '-fecha_creacion']

class ImagenVehiculo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='vehiculos/%Y/%m/')
    es_principal = models.BooleanField(default=False, help_text="Marcar si es la foto principal de portada")
    orden = models.PositiveIntegerField(default=0, help_text="Orden de visualización (menor = primero)")

    def __str__(self):
        return f"Imagen de {self.vehiculo.marca.nombre} {self.vehiculo.modelo}"

    class Meta:
        verbose_name = "Imagen de Vehículo"
        verbose_name_plural = "Imágenes de Vehículos"
        ordering = ['orden', '-es_principal', 'id']
