from blog.models import Category

def all_categories(request):
    contex = {
        'miscategorias':Category.objects.all()
    }
    return contex