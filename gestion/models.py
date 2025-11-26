from django.db import models
from django.contrib.auth.models import User 

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    nota_promedio = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"