from django import forms
from .models import PilotosClass

class PilotoForm(forms.ModelForm):
    class Meta:
        model = PilotosClass
        fields = ['name']