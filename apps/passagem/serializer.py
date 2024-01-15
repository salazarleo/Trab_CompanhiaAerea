# serializers.py
from rest_framework import serializers
from .models import PassagensClass

class PassagensClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassagensClass
        fields = '__all__'
