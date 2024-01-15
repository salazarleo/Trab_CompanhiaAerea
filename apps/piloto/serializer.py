from .models import PilotosClass
from rest_framework import serializers

class PilotoClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PilotosClass
        fields = '__all__'