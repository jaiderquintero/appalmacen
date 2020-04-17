from django.urls import path

app_name ='clients'
urlpatterns = [
    path('', index, name='clients'),  # Donde index es el metodo o vista que se encuentra en app/clients/index

]