from django.urls import path
# from django.contrib.auth.views import views as auth_views

from . import views

urlpatterns = [
    path('event_view/', views.event_view, name='event_view'),
    path('event_delete/<int:pk>/', views.event_delete, name='event_delete'),
    path('event_update/<int:pk>/', views.event_update, name='event_update'),
    path('<m>/', views.calendario, name='calendario'),
    path('', views.calendario_base, name='calendario_base'),
    path('addevent/<int:year>/<int:month>/<int:d>/', views.event_create, name='addevent'),
    # path('addevent/', views.event_create, name='addevent')
    # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.registrar_user, name='registrar_user'),
]