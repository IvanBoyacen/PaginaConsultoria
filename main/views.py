from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import View


def index(request):
    return render(request, 'LandingPage.html')

def login_view(request):
    return render(request, 'registration/login.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        # Obtener las credenciales del usuario
        username = request.POST['username']
        password = request.POST['password']
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Iniciar sesión
            login(request, user)
            # Redireccionar al menú principal
            return redirect('principal')
        else:
            # Las credenciales son inválidas, mostrar un mensaje de error
            error_message = "Las credenciales son inválidas. Por favor, inténtelo de nuevo."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # Si no se envió un formulario POST, mostrar la página de inicio de sesión
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def principal(request):
    titulo="Menu principal"
    context={
        'titulo':titulo
    }
    return render(request,'Menu.html',context)

class ResetPasswordView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/forgotPassword.html')
    
def formulario_contacto(request):
    return render(request, 'contacto.html')

def Matnaftblog(request):
    return render(request, 'LandingPage.html')
