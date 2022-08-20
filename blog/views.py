from email import message
from gc import get_objects
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Category
from .form import CatForm, PostForm
# Create your views here.

def post_list(request):
    post = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'post': post})

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

def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blog/blog_update.html', {'form': form, 'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('post_list')

def post_view(request, pk):
    post = Post.objects.all(id=pk)
    return render(request, 'blog/blog_view.html', {'post': post})

def category_view(request):
    cat = Category.objects.all()
    form = CatForm()
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Nueva categoria agregada')
            return redirect('category_view')
    form = CatForm()
    return render(request, 'blog/allcategory.html', {'cat': cat, 'form': form})

def category_update(request, pk):
    cat = Category.objects.all()
    cat_edit = get_object_or_404(Category, id=pk)
    data = cat_edit
    form = CatForm(request.POST, instance=cat_edit)
    if form.is_valid():
        form.save()
        return redirect('category_view')
    return render(request, 'blog/allcategory_edit.html', {'form': form, 'cat': cat, 'cat_edit': cat_edit, 'data': data})

# def post_delete(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     post.delete()
#     return redirect('post_list')