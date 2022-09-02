from distutils.command.upload import upload
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

from django.template.defaultfilters import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    describe = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    created_at_time =models.TimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    updated_at_time = models.TimeField(auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    num_views = models.IntegerField('Numero de visitas', default=0)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    def __str__(self):
        return self.content[:10]


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name