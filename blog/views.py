from email import message
from gc import get_objects
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Category, Comment
from .form import CatForm, PostForm, CommentForm
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
    data = post
    form = PostForm(initial={'title':data.title, 'content':data.content, 'active':data.active, 'category':data.category})
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    return render(request, 'blog/blog_update.html', {'form': form, 'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('post_list')

def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # post = Post.objects.all(id=pk)
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
    form = CatForm(initial={'name':data.name})
    if request.method == 'POST':
        form = CatForm(request.POST, instance=cat_edit)
        if form.is_valid():
            form.save()
            return redirect('category_view')
    return render(request, 'blog/allcategory_edit.html', {'form': form, 'cat': cat, 'cat_edit': cat_edit, 'data': data})

def cat_delete(request, pk):
    cat = get_object_or_404(Category, id=pk)
    cat.delete()
    return redirect('category_view')

def categoris(request, pk):
    post = Post.objects.filter(category__id=pk)
    # post = Post.objects.all(category.id=pk)
    return render(request, 'blog/blog_cate.html', {'post':post})

def comment_create(request, slug):
    context = {}
    post = get_object_or_404(Post, slug=slug)
    context['post'] = post
    form = CommentForm()
    context['form'] = form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_view', slug=post.slug)
    return render(request, 'blog/comment_create.html', context)

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    comment.delete()
    return redirect('post_view', slug=comment.post.slug)

def comment_update(request, pk):
    context = {}
    comment = get_object_or_404(Comment, id=pk)
    data = comment
    context['commen'] = comment
    form = CommentForm(initial={'content':data.content})
    context['form'] = form
    context['post'] = comment.post
    post = comment.post
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_view', slug=post.slug)
    return render(request, 'blog/comment_update.html', context)
    
    # comment = get_object_or_404(Comment, id=pk)
    # data = comment
    # form = CommentForm(initial={'content':data.content})
    # if request.method == 'POST':
    #     form = CommentForm(request.POST, instance=comment)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('post_view', slug=comment.post.slug)
    # return render(request, 'blog/comment_update.html', {'form': form})