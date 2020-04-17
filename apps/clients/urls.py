from django.urls import path
from apps.clients.views import index, listClients

app_name ='clients'
urlpatterns = [
    path('listar', listClients, name='listClients'),  # Donde index es el metodo o vista que se encuentra en app/clients/index

]