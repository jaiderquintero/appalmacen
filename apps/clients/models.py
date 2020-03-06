from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    lastname = models.CharField(max_length=50, verbose_name="Apellidos")
    rut = models.CharField(max_length=20, verbose_name="Cedula")
    address = models.CharField(max_length=50, verbose_name="Direccion")
    phone = models.CharField(max_length=50, verbose_name="Telefono")
    #email = models.CharField(max_length=50, verbose_name="Correo Electronico")

    def __str__(self):
        return self.name + " " + self.lastname

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
