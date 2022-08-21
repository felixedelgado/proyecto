from dataclasses import fields
from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user', 'slug']
    

class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    name = forms.CharField(max_length=255) # Esto agrego para poder darle estilo al formulario con css sin crispy