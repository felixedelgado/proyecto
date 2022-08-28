import http
from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from blog.models import Category
from blog.form import CatForm
from django.contrib import messages
# from .models import Post


# def index(resquest):
#     # posts = Post.objects.all()
#     return HttpResponse('Hola Mundo')
#     # return HttpResponse('Hola Mundo', posts)

# def index(request):
#     return render(request, 'home/index.html')

# def category_view(request):
#     cat = Category.objects.all()
#     form = CatForm()
#     if request.method == 'POST':
#         form = CatForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, 'Nueva categoria agregada')
#             return redirect('category_view')
#     form = CatForm()
#     return render(request, 'home/templates/base.html', {'cat': cat, 'form': form})

def index(request):
    # cat = Category.objects.all()
    # form = CatForm()
    # if request.method == 'POST':
    #     form = CatForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # messages.success(request, 'Nueva categoria agregada')
    #         return redirect('index')
    # form = CatForm()
    # return render(request, 'home/index.html', {'cat_global': cate_global })
    return render(request, 'home/index.html')
