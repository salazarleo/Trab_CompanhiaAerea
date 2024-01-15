from .models import AvioesClass
from rest_framework import serializers

class AvioesClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvioesClass
        fields = '__all__'