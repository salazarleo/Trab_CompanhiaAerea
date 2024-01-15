from django.db import models
from aviao.models import AvioesClass
from passageiro.models import PassageirosClass

class PassagensClass(models.Model):
    ID = models.AutoField(primary_key=True)
    nome = models.ForeignKey(PassageirosClass, on_delete=models.CASCADE)
    destino = models.ForeignKey(AvioesClass, on_delete=models.CASCADE)
    assento = models.CharField('Assento', max_length=5)
    horario = models.CharField('Horario', max_length=5)
    portao = models.CharField('Portao', max_length=3)
    
    class Meta:
        verbose_name = 'Passagem'
        verbose_name_plural = 'Passagens'
        ordering = ['ID']

    def __str__(self):
        return str(self.ID)