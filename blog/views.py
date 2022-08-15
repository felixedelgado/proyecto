from email import message
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .form import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post guardado con exito')
            return redirect('post_list')
        messages.error(request, 'Hay errores en el Post')
    form = PostForm()
    return render(request, 'blog/blog_create.html', {'form': form})