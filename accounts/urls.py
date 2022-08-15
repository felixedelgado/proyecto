from django.urls import path
# from django.contrib.auth.views import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registrar_user, name='registrar_user'),
]