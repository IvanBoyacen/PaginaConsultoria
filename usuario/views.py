from django.shortcuts import render, redirect

def usuarios(request):
    titulo = "Usuarios"
    context = {
        'titulo': titulo,
        'usuarios': usuarios
    }
    return render(request, 'usuario/usuarios.html', context)

