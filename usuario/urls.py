from django.urls import path
from usuario.views import usuarios

urlpatterns = [
    
path( '',usuarios,name="Usuarios"),

]