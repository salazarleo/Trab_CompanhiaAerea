from django import forms
from .models import PassageirosClass

class PassageiroForm(forms.ModelForm):
    class Meta:
        model = PassageirosClass
        fields = '__all__'  # Isso incluirá todos os campos do modelo no formulário