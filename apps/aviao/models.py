from django.db import models
from piloto.models import PilotosClass
# Create your models here.

class AvioesClass(models.Model):
    piloto = models.ForeignKey(PilotosClass, on_delete=models.CASCADE)
    modelo = models.TextField('Modelo', max_length=15)
    destino = models.TextField('Destino', max_length=30)
    capacidade = models.CharField('Capacidade', max_length=3)
    
    class Meta:
        verbose_name = 'Aviao'
        verbose_name_plural = 'Avioes'
        ordering =['id']

    def __str__(self):
        return self.destino