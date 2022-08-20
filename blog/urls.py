from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add/', views.post_create, name='post_create'),
    path('allcategory/', views.category_view, name='category_view'),
    path('allcategory/edit/<int:pk>', views.category_update, name='edit_category'),
    path('update/<int:pk>/', views.post_update, name='post_update'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('view/<int:pk>/', views.post_view, name='post_view'),
]