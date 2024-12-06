from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono", blank=True, null=True)
    puesto = models.CharField(max_length=100, verbose_name="Puesto de Trabajo")
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salario")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.puesto}"
