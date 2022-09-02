from email import message
from gc import get_objects
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Category, Comment
from .form import CatForm, PostForm, CommentForm
# from accounts.utils import has_admin

from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def post_list(request):
    post = Post.objects.filter(active=True).order_by('-created_at', '-created_at_time')
    return render(request, 'blog/blog_list.html', {'post': post})

def post_date(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        if fecha:
            post = Post.objects.filter(created_at=fecha).order_by('-created_at_time')
            return render(request, 'blog/blog_date.html', {'post':post, 'fecha':fecha})
        else:
            post = Post.objects.all().order_by('-created_at_time')
            return render(request, 'blog/blog_date.html', {'post':post})
    else:
        post = Post.objects.all().order_by('-created_at_time')
        return render(request, 'blog/blog_date.html', {'post':post})
    
@login_required
def post_date_edit(request):
    if not request.user.is_admin:
        return redirect('index')
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        if fecha:
            post = Post.objects.filter(updated_at=fecha).order_by('-updated_at_time')
            return render(request, 'blog/blog_date_edit.html', {'post':post, 'fecha':fecha})
        else:
            post = Post.objects.all().order_by('-updated_at_time')
            return render(request, 'blog/blog_date_edit.html', {'post':post})
    else:
        post = Post.objects.all().order_by('-updated_at_time')
        return render(request, 'blog/blog_date_edit.html', {'post':post})

@login_required
# @user_passes_test(has_admin)
def post_create(request):
    if not request.user.is_admin:
        return redirect('index')
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

@login_required
def post_update(request, pk):
    if not request.user.is_admin:
        return redirect('index')
    post = get_object_or_404(Post, id=pk)
    data = post
    form = PostForm(initial={'title':data.title, 'describe':data.describe, 'content':data.content, 'active':data.active, 'category':data.category, 'image':data.image})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    return render(request, 'blog/blog_update.html', {'form': form, 'post': post})

@login_required
def post_delete(request, pk):
    if not request.user.is_admin:
        return redirect('index')
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('post_list')

def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if not request.user.is_authenticated:
        post.num_views = post.num_views + 1
    elif not request.user.is_admin:
        post.num_views = post.num_views + 1
    post.save()
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

@login_required
def post_inactive(request):
    if not request.user.is_admin:
        return redirect('index')
    post = Post.objects.filter(active=False)
    return render(request, 'blog/blog_inact.html', {'post':post})

@login_required
def category_update(request, pk):
    if not request.user.is_admin:
        return redirect('index')
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

@login_required
def cat_delete(request, pk):
    if not request.user.is_admin:
        return redirect('index')
    cat = get_object_or_404(Category, id=pk)
    cat.delete()
    return redirect('category_view')

def categoris(request, pk):
    post = Post.objects.filter(category__id=pk, active=True).order_by('-created_at', '-created_at_time')
    # post = Post.objects.all(category.id=pk)
    return render(request, 'blog/blog_cate.html', {'post':post})

@login_required
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
    return render(request, 'blog/blog_view.html', context)

@login_required
def comment_delete(request, pk):
    if request.user.is_admin:
        comment = get_object_or_404(Comment, id=pk)
    else:
        comment = get_object_or_404(Comment, id=pk, user=request.user)
    comment.delete()
    return redirect('post_view', slug=comment.post.slug)

@login_required
def comment_update(request, pk):
    context = {}
    if request.user.is_admin:
        comment = get_object_or_404(Comment, id=pk)
    else:
        comment = get_object_or_404(Comment, id=pk, user=request.user)
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
    