from django.shortcuts import render, redirect
from .models import PassageirosClass
from rest_framework import viewsets
from .serializer import PassageirosClassSerializer
from .forms import PassageiroForm

class PassageirosClassViewSet(viewsets.ModelViewSet):
    queryset = PassageirosClass.objects.all()
    serializer_class = PassageirosClassSerializer

def criar_passageiro(request):
    if request.method == 'POST':
        form = PassageiroForm(request.POST)
        if form.is_valid():
            form.save()
            passageiros = PassageirosClass.objects.all()
            return render(request, 'passageiro/criar_passageiro.html', {'form': form, 'passageiros': passageiros})
    else:
        form = PassageiroForm()

    return render(request, 'passageiro/criar_passageiro.html', {'form': form})

def lista_passageiros(request):
    passageiros = PassageirosClass.objects.all()
    return render(request, 'passageiro/lista_passageiros.html', {'passageiros': passageiros})