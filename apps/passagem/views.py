# views.py

from django.views import View
from .models import PassagensClass
from .serializer import PassagensClassSerializer
from django.shortcuts import render, redirect
from .forms import CriarPassagemForm
from django.views import View
from django.http import JsonResponse
from .models import PassagensClass

from django.shortcuts import render, redirect

class CriarPassagemView(View):
    template_name = 'passagem/criar_passagem.html'

    def post(self, request, *args, **kwargs):
        form = CriarPassagemForm(request.POST)
        if form.is_valid():
            form.save()
            passagens = PassagensClass.objects.all()
            return render(request, self.template_name, {'form': form, 'passagens': passagens})
        
        # If form is not valid, render the same page with errors
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = CriarPassagemForm()
        passagens = PassagensClass.objects.all()
        return render(request, self.template_name, {'form': form, 'passagens': passagens})

    
class ListarPassagensView(View):
    template_name = 'passagem/listar_passagens.html'

    def get(self, request, *args, **kwargs):
        passagens = PassagensClass.objects.all()
        return render(request, self.template_name, {'passagens': passagens})
    
class VerPassagensView(View):
    template_name = 'passagem/ver_passagens.html'

    def get(self, request, *args, **kwargs):
        passagens = PassagensClass.objects.all()
        return render(request, self.template_name, {'passagens': passagens})