from django.db import models

# Create your models here.

class PassageirosClass(models.Model):
    nome = models.TextField('Nome', max_length=50)
    email = models.EmailField('Email', max_length=50)
    cpf = models.CharField('CPF', max_length=11)
    telefone = models.CharField('Telefone', max_length=20)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    genero = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    
    class Meta:
        verbose_name = 'Passageiro'
        verbose_name_plural = 'Passageiros'
        ordering =['id']

    def __str__(self):
        return self.nome