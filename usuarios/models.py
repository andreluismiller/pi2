from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_consumidor = models.BooleanField(default=False)
    is_produtor = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Consumidor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    whatsapp_number = models.CharField(max_length=20)
    endereco = models.CharField(max_length=20)

class Produtor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    whatsapp_number = models.CharField(max_length=20)
    endereco = models.CharField(max_length=20)