from dataclasses import fields
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
    name = forms.CharField(max_length=50)
    date = forms.DateField()
    hora = forms.TimeField()
    descripcion = forms.CharField(max_length=150)
    lugar = forms.CharField(max_length=70)

class EventForm1(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['date']