from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Consumidor,Produtor

class ConsumidorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    whatsapp_number = forms.CharField(required=True)
    endereco = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_consumidor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        consumidor = Consumidor.objects.create(user=user)
        consumidor.whatsapp_number=self.cleaned_data.get('whatsapp_number')
        consumidor.endereco=self.cleaned_data.get('endereco')
        consumidor.save()
        return user

class ProdutorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    whatsapp_number = forms.CharField(required=True)
    endereco = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        produtor = Produtor.objects.create(user=user)
        produtor.whatsapp_number=self.cleaned_data.get('phone_number')
        produtor.endereco=self.cleaned_data.get('designation')
        produtor.save()
        return user