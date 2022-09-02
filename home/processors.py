from blog.models import Category, Post

def all_categories(request):
    contex = {
        'miscategorias':Category.objects.all(),
        'mispost':Post.objects.all()
    }
    return contex

