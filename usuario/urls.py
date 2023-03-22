from django.urls import path
from usuario.views import usuario

urlpatterns = [
    
path( '',usuario,name="usuarios"),

]