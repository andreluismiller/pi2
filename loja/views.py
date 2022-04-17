from django.shortcuts import render
from .models import *

def home(request):
    produtos = Produto.objects.all()
    context = {'produtos':produtos}
    return render(request, 'loja/home.html', context)

def lista(request):

    if request.user.is_authenticated:
        consumidor = request.user.consumidor
        lista, created = Lista.objects.get_or_create(consumidor=consumidor)
        items = lista.itemlista_set.all()
    else:
        items = []
        lista = {'get_total_lista': 0, 'get_total_items': 0}

    context= {'items':items, 'lista':lista}
    return render(request, 'loja/lista.html', context)



def finalizar(request):
    context = {}
    return render(request, 'loja/finalizar.html', context)