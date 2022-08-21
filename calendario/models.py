from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.TextField('Nombre del evento', max_length=50)
    date = models.DateTimeField('Dia del evento')
    descripcion = models.TextField(blank=True, max_length=150)
    lugar = models.CharField(max_length=70)

    # def __str__(self):
    #     return super().name