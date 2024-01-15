# passagem/forms.py
from django import forms
from .models import PassagensClass

class CriarPassagemForm(forms.ModelForm):
    class Meta:
        model = PassagensClass
        fields = '__all__'
