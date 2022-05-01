from django.contrib import admin

from usuarios.models import User
from . models import *

admin.site.register(Produto)
admin.site.register(Lista)
admin.site.register(ItemLista)
