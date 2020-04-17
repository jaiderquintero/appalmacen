from django.shortcuts import render
from django.shortcuts import redirect
from apps.clients.models import Client

# Create your views here.

def index(request):
    return render(request, 'clients/index.html')

def listClients(request):
    client = Client.objects.all().order_by('-id')
    context = {'clients':client}
    return render(request, 'clients/listClients.html', context)