from django.urls import path
from .import  views

urlpatterns=[
     path('register/',views.register, name='cadastro'),
     path('cadastro_consumidor/',views.consumidor_register.as_view(), name='consumidor_register'),
     path('cadastro_produtor/',views.produtor_register.as_view(), name='produtor_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]