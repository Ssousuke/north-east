from django.urls import path
from . import views

app_name = 'publication'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('noticias/<str:slug>/', views.detail, name='detail'),
]
