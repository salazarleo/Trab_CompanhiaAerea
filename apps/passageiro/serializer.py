from .models import PassageirosClass
from rest_framework import serializers

class PassageirosClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassageirosClass
        fields = '__all__'