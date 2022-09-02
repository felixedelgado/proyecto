from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField('Nombre del evento', max_length=50)
    date = models.DateField('Dia del evento')
    hora = models.TimeField('Hora del evento')
    descripcion = models.CharField(blank=True, max_length=150)
    lugar = models.CharField(max_length=70)

    # def __str__(self):
    #     return super().name