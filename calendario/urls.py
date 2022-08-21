from django.urls import path
# from django.contrib.auth.views import views as auth_views

from . import views

urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('addevent/<year>/<month>/<d>/', views.event_create, name='addevent')
    # path('addevent/', views.event_create, name='addevent')
    # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.registrar_user, name='registrar_user'),
]