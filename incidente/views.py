from django.shortcuts import render, redirect
from .forms import IncidenteForm
from .models import Incidente

# Create your views here.
def incidentes(request):
    titulo = "Incidentes"
    context = {
        'titulo': titulo,
        'incidentes': incidentes
    }
    return render(request, 'incidente/incidente.html', context)



def crear_incidente(request):
    if request.method == 'POST':
        form = IncidenteForm(request.POST, request.FILES)
        if form.is_valid():
            incidente = form.save()
            return redirect('detalle_incidente', pk=incidente.pk)
    else:
        form = IncidenteForm()
    return render(request, 'incidente/crear_incidente.html', {'form': form})

def detalle_incidente(request, pk):
    incidente = Incidente.objects.get(pk=pk)
    return render(request, 'incidente/detalle_incidente.html', {'incidente': incidente})
