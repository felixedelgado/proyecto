import http
from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from blog.models import Category
from blog.form import CatForm
from django.contrib import messages
from blog.models import Post


def index(request):
    # busqueda = request.GET.get('busqueda', '')
    # post = Post.object.filter(title__icontains=busqueda)[:3]
    return render(request, 'home/index.html')
