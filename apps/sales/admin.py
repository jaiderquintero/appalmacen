from django.contrib import admin

# Register your models here.

from apps.sales.models import Sale, SaleProduct

admin.site.register(Sale)
admin.site.register(SaleProduct)