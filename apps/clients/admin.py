from django.contrib import admin

# Register your models here.
from apps.clients.models import Client

class ClientAdmin(admin.ModelAdmin):
    # readonly_fields = ('created', 'updated') #No permite edicion de create y update
    list_display = ('name', 'lastname', 'rut', 'address', 'phone')
    ordering = ('name', 'lastname', 'rut', 'address', 'phone')  # En caso que sea una sola ordering('column',)
    #form de busqueda
    search_fields = ('name','lastname', 'rut') #Campo relacionado
    #date_hierarchy = 'create'    #campo de fechas
    list_filter = ('name', 'lastname',) # Campos relacionados

admin.site.register(Client, ClientAdmin)
