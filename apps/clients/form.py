from django.forms import ModelForm
from apps.clients.models import Client

class ClientForm(ModelForm):
    
    class Meta:
        model = Client

        fields = [
            'name',
            'lastname',
            'rut',
            'address',
            'phone',
        ]

        labels = {
            'name': 'Nombre',
            'lastname': 'Apellidos',
            'rut': 'Rut',
            'address': 'Direccion',
            'phone': 'Telefono',
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            # 'product_types':forms.Select(attrs={'class':'form-control'}),  #para realacion 1 a muchos y forms.CheckboxSelectMultiple muchos a muchos
        }