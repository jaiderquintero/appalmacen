from django.contrib import admin

# Register your models here.
from apps.products.models import ProductType, Product

admin.site.register(ProductType)
admin.site.register(Product)
