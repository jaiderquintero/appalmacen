from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    quantity = models.IntegerField(verbose_name="Cantidad")
    price = models.IntegerField(verbose_name="Precio")
    description = models.TextField(verbose_name="Descripcion")
    mark = models.CharField(max_length=50, verbose_name="Marca")
    product_types = models.ForeignKey(ProductType,
                                    null=True,
                                    blank=True,
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = " productos"
