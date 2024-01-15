# apps/aviao/forms.py
from django import forms
from .models import AvioesClass

class AviaoForm(forms.ModelForm):
    class Meta:
        model = AvioesClass
        fields = ['piloto', 'modelo', 'destino', 'capacidade']
