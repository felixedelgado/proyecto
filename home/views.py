import http
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(resquest):
    return HttpResponse('Hola Mundo')