# apps/aviao/views.py
from django.shortcuts import render, redirect
from .models import AvioesClass
from rest_framework import viewsets
from .serializer import AvioesClassSerializer
from .forms import AviaoForm

class AvioesClassViewSet(viewsets.ModelViewSet):
    queryset = AvioesClass.objects.all()
    serializer_class = AvioesClassSerializer  

def criar_aviao(request):
    if request.method == 'POST':
        form = AviaoForm(request.POST)
        if form.is_valid():
            form.save()
            # Recupere a lista de avioes e passe para o contexto
            avioes = AvioesClass.objects.all()
            return render(request, 'criar_aviao.html', {'form': form, 'avioes': avioes})
        
    else:
        form = AviaoForm()

    return render(request, 'criar_aviao.html', {'form': form})

def aviao_detail(request, aviao_id):
    aviao = get_object_or_404(AvioesClass, pk=aviao_id)
    return render(request, 'aviao_detail.html', {'aviao': aviao})

def lista_avioes(request):
    avioes = AvioesClass.objects.all()
    return render(request, 'lista_avioes.html', {'avioes': avioes})