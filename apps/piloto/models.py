from django.db import models

# Create your models here.

class PilotosClass(models.Model):
    
    name = models.CharField('Nome', max_length=50)
    
    class Meta:
        verbose_name = 'Piloto'
        verbose_name_plural = 'Pilotos'
        ordering =['id']

    def __str__(self):
        return self.name