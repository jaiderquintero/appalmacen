from django.urls import path
from apps.clients.views import index, listClients, clientCreate, clientEdit, clientDelete

app_name ='clients'
urlpatterns = [
    path('listar', listClients, name='listClients'),  # Donde index es el metodo o vista que se encuentra en app/clients/index
    path('nuevo/', clientCreate, name='clientCreate'),
    path('editar/<int:id_client>/', clientEdit, name='clientEdit'),
    path('eliminar/<int:id_client>/', clientDelete, name='clientDelete'),
]