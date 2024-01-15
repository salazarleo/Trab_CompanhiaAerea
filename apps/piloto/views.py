from django.shortcuts import render, redirect
from .models import PilotosClass
from rest_framework import viewsets
from .serializer import PilotoClassSerializer
from .forms import PilotoForm

# Create your views here.

class PilotosClassViewSet(viewsets.ModelViewSet):
    queryset = PilotosClass.objects.all()
    serializer_class = PilotoClassSerializer 

def criar_piloto(request):
    if request.method == 'POST':
        form = PilotoForm(request.POST)
        if form.is_valid():
            form.save()
            # Recupere a lista de pilotos e passe para o contexto
            pilotos = PilotosClass.objects.all()
            return render(request, 'criar_piloto.html', {'form': form, 'pilotos': pilotos})
    else:
        form = PilotoForm()

    # Se for uma solicitação GET, apenas renderize o formulário de criação de piloto
    return render(request, 'criar_piloto.html', {'form': form})

def lista_pilotos(request):
    pilotos = PilotosClass.objects.all()
    return render(request, 'lista_pilotos.html', {'pilotos': pilotos})