from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.categoris, name='blog_cate'),
    path('inactive/', views.post_inactive, name='blog_inactivos'),
    path('add/', views.post_create, name='post_create'),
    path('allcategory/', views.category_view, name='category_view'),
    path('allcategory/edit/<int:pk>', views.category_update, name='edit_category'),
    path('allcategory/delete/<int:pk>', views.cat_delete, name='cat_delete'),
    path('update/<int:pk>/', views.post_update, name='post_update'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('view/<slug:slug>/', views.post_view, name='post_view'),
    path('view/<slug:slug>/comments/add/', views.comment_create, name='comment_create'),
    path('comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('comments/<int:pk>/update/', views.comment_update, name='comment_update'),
]