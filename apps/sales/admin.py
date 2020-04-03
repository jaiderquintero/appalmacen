from django.contrib import admin

# Register your models here.
from apps.sales.models import Sale, SaleProduct

class MembershipInline(admin.TabularInline):
    model = SaleProduct
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

class SaleAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    # readonly_fields = ('created', 'updated')  # No permite edicion de create y update
    list_display = ('date','user', 'discount', 'clients', 'subtotal', 'total')
    ordering = ('date', 'user', 'clients', 'total')
    search_fields = ('date','user__username', 'clients__name') #Campo relacionado
    list_filter = ('date', 'user__username','clients__name',) # Campos relacionados
    date_hierarchy = 'date'

    def sale_products(self, obj):
        return ". ".join([c.name for c in obj.products.all().order_by("date")])

    sale_products.short_description = "Productos"

admin.site.register(Sale, SaleAdmin)