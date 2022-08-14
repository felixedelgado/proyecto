import http
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
# from .models import Post


# def index(resquest):
#     # posts = Post.objects.all()
#     return HttpResponse('Hola Mundo')
#     # return HttpResponse('Hola Mundo', posts)

def index(resquest):
    return render(resquest, 'home/index.html')
