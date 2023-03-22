from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib import messages



def principal(request):
    titulo="Menu principal"
    context={
        'titulo':titulo
    }
    return render(request,'menu.html',context)