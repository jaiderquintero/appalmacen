from django.shortcuts import render
from django.shortcuts import redirect
from apps.clients.models import Client
from apps.clients.form import ClientForm

# Create your views here.

def index(request):
    return render(request, 'clients/index.html')

def listClients(request):
    client = Client.objects.all().order_by('-id')
    context = {'clients':client}
    return render(request, 'clients/listClients.html', context)

def clientCreate(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('clients:listClients')
    else:
        form = ClientForm()
    return render(request, 'clients/formClient.html', {'form':form})

def clientEdit(request, id_client):
    client = Client.objects.get(pk=id_client)
    if request.method == 'GET':
        form = ClientForm(instance=client)
    else:
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
        return redirect('clients:listClients')

    return render(request, 'clients/formClient.html', {'form':form})

def clientDelete(request, id_client):
    client = Client.objects.get(pk=id_client)
    
    if request.method == 'POST':
        client.delete()
        return redirect('clients:listClients')
    return render(request, 'clients/clientDelete.html', {'clients': client})